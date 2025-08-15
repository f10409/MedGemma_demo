import matplotlib.pyplot as plt
import numpy as np

def display_prediction(output, example, figsize=(8, 6)):
    """
    Display an image with prediction and label information.
    
    Args:
        output: Model output containing input_text with image data and generated_text
        example: Example data containing the true label under 'Pathology' key
        figsize: Figure size as (width, height) tuple (default: (8, 6))
    """
    img_arr = np.array(output[0]['input_text'][1]['content'][-1]['image'])
    plt.figure(figsize=figsize)
    plt.imshow(img_arr)
    plt.title(f'Prediction: {output[0]["generated_text"].strip()}\nLabel: {example["Pathology"]}')
    plt.axis('off')
    plt.show()