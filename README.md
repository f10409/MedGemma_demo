# MedGemma Demo
Chest X-ray visual question answering (VQA) and classification, radiology report generation, and anatomy localization with MedGemma 1.5 (`google/medgemma-1.5-4b-it`).

**Frank Li** | HITI Lab, Emory University | Datathon

## Notebooks
| Notebook | What it does | Colab |
|---|---|---|
| `0_hugging_face.ipynb` | Hugging Face login and MedGemma 1.5 access check | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/f10409/MedGemma_demo/blob/main/0_hugging_face.ipynb) |
| `1_medgemma_demo.ipynb` | VQA and classification, report generation, anatomy localization | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/f10409/MedGemma_demo/blob/main/1_medgemma_demo.ipynb) |

## Usage (Google Colab)
1. Open `0_hugging_face.ipynb` in Colab. Accept the MedGemma 1.5 terms and save your token as the `HF_TOKEN` secret.
2. Open `1_medgemma_demo.ipynb` in Colab. Select **Runtime → Change runtime type → T4 GPU**. When Colab asks for access to the `HF_TOKEN` secret, click **Grant access**.
3. Run all cells. The first code cell gets the helper code and installs [RadHarmony](https://github.com/f10409/RadHarmony).

## Data
The demo uses the open-access [Open-i Indiana University chest X-ray collection](https://openi.nlm.nih.gov/faq) (3,955 reports, 7,470 images). The notebook downloads it (about 1.4 GB) and loads it with RadHarmony (`OpenICXRHarmonizer`, `OpenICXRDataset`).

Citation: Demner-Fushman D, et al. Preparing a collection of radiology examinations for distribution and retrieval. *JAMIA*. 2016;23(2):304–310.

## Local Installation
```bash
git clone https://github.com/f10409/MedGemma_demo.git
cd MedGemma_demo
uv sync
source .venv/bin/activate
python -m ipykernel install --user --name medgemma
```
Log in to Hugging Face with `hf auth login` (or run `0_hugging_face.ipynb`). Then launch Jupyter and select the `medgemma` kernel. The data downloads to `data/OpenI-IU-CXR/`.
