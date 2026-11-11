import gradio as gr

from utils.localization import boxes_on_image, pad_to_square, remove_thinking
from utils.preprocess import preprocess
from utils.report import extract_findings

# Empty VQA answer, generated findings, box image, and localization answer
CLEARED = ("", "", None, "")


def app_image(image):
    """Make an image ready for the model (8-bit RGB). Also works for 16-bit images."""
    if image.mode in ("RGBA", "LA", "P"):  # Remove transparency and color tables
        image = image.convert("RGB")
    return preprocess(image)


def make_app(pipe, examples, system_message, localize, default_index=56):
    """
    Build a Gradio app with an Open-i image list and 3 tabs: VQA, report generation, and localization.

    Args:
        pipe: The MedGemma pipeline.
        examples: List of sample dicts ("ImagePath", "Pathology", "Report", "Findings", "Indication").
        system_message: System message for all prompts.
        localize: Function (square image, body part) -> (boxes, answer).
        default_index: Sample that the app shows first.

    Returns:
        gr.Blocks: The app. Start it with demo.launch().
    """

    def messages(image, text):
        """Make the messages for one image and one prompt."""
        return [
            system_message,
            {
                "role": "user",
                "content": [
                    {"type": "image", "image": app_image(image)},
                    {"type": "text", "text": text},
                ],
            },
        ]

    def generate(image, text):
        """Run the model on one image and one prompt. Return the generated text."""
        output = pipe(text=messages(image, text), max_new_tokens=300, return_full_text=False)
        return output[0]["generated_text"].strip()

    def app_vqa(image, question):
        """Answer a question about the image."""
        if image is None or not question.strip():
            return "Pick or upload an image. Then type a question."
        return remove_thinking(generate(image, question))  # Some questions start a thinking trace

    def app_report(image, indication):
        """Write the findings, with the same prompt as the report section."""
        if image is None:
            return "Pick or upload an image."
        indication = indication.strip()
        prompt = f"{indication} findings:" if indication else "findings:"
        return extract_findings(generate(image, prompt))

    def app_localize(image, object_name):
        """Find one body part. Return the image with the box, and the answer."""
        if image is None or not object_name.strip():
            return None, "Pick or upload an image. Then type a body part."
        square = pad_to_square(app_image(image))
        boxes, answer = localize(square, object_name)
        boxes = [{"box_2d": b["box_2d"], "label": object_name} for b in boxes]
        return boxes_on_image(square, boxes), answer

    def app_load_example(index):
        """Show one sample, its indication, true findings, and label. Clear old answers."""
        example = examples[index]
        # Some reports have no findings section, so use the full report
        true_findings = example["Findings"] or example["Report"]
        label = f"**Label:** {example['Pathology']}"
        return example["ImagePath"], example["Indication"] or "", true_findings, label, *CLEARED

    def app_upload():
        """Clear the sample text and the old answers after you upload your own image."""
        return "", "", "**Label:** none (your own image)", *CLEARED

    gr.close_all()  # Stop the old app if you build the app again
    image_choices = [(f"{i}: {ex['Pathology']}", i) for i, ex in enumerate(examples)]

    with gr.Blocks(title="MedGemma 1.5") as demo:
        gr.Markdown("# MedGemma 1.5\nFor research and education only. Do not use for patient care.")
        with gr.Row():
            with gr.Column():
                image_choice = gr.Dropdown(image_choices, value=default_index, label="Open-i image")
                image_label = gr.Markdown()
                image = gr.Image(type="pil", image_mode=None, label="Chest X-ray (or upload your own)")

            with gr.Column():
                with gr.Tab("VQA"):
                    vqa_question = gr.Textbox(
                        label="Question", value="What abnormal findings do you see in this chest X-ray?"
                    )
                    vqa_button = gr.Button("Ask", variant="primary")
                    vqa_answer = gr.Textbox(label="Answer", lines=8)

                with gr.Tab("Report generation"):
                    report_indication = gr.Textbox(label="Indication (optional)")
                    report_button = gr.Button("Write findings", variant="primary")
                    report_text = gr.Textbox(label="Generated findings", lines=8)
                    report_true = gr.Textbox(label="True findings (radiologist)", lines=6)

                with gr.Tab("Anatomy localization"):
                    loc_object = gr.Textbox(label="Body part", value="right lung")
                    loc_button = gr.Button("Find", variant="primary")
                    loc_answer = gr.Textbox(label="Answer", lines=4)
                    loc_result = gr.Image(label="Box (on the square image)")

        # Show the selected Open-i image when the app opens and when you pick an image
        text_outputs = [report_indication, report_true, image_label]
        old_answers = [vqa_answer, report_text, loc_result, loc_answer]
        gr.on(
            [demo.load, image_choice.select],
            app_load_example,
            image_choice,
            [image, *text_outputs, *old_answers],
        )
        image.upload(app_upload, None, [*text_outputs, *old_answers])

        # The 3 tabs share one GPU, so they wait in one queue (one request at a time)
        vqa_button.click(app_vqa, [image, vqa_question], vqa_answer, concurrency_id="model")
        report_button.click(app_report, [image, report_indication], report_text, concurrency_id="model")
        loc_button.click(app_localize, [image, loc_object], [loc_result, loc_answer], concurrency_id="model")

    return demo
