# MedGemma Demo
Chest X-ray visual question answering (VQA) and classification, radiology report generation, and anatomy localization with MedGemma 1.5 (`google/medgemma-1.5-4b-it`).

**Frank Li, Judy Gichoya, Mohammadreza Chavoshi** | HITI Lab, Emory University | RSNA 2026 Deep Learning Lab

## Notebook
| Notebook | What it does | Colab |
|---|---|---|
| `1_medgemma_demo.ipynb` | Data download, Hugging Face access, VQA and classification, report generation, anatomy localization, web app | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/f10409/MedGemma_demo/blob/main/1_medgemma_demo.ipynb) |

## Usage (Google Colab)
1. Open `1_medgemma_demo.ipynb` in Colab. Select **Runtime → Change runtime type → T4 GPU**.
2. Run the first code cell. It gets the helper code and downloads the data. While it runs, accept the MedGemma 1.5 terms and save your Hugging Face token as the `HF_TOKEN` secret (Step 2 in the notebook).
3. Run the other cells. The setup cell installs [RadHarmony](https://github.com/f10409/RadHarmony) and checks your access. When Colab asks for access to the `HF_TOKEN` secret, click **Grant access**.

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
Log in to Hugging Face with `hf auth login`. Then launch Jupyter and select the `medgemma` kernel. The data downloads to `data/OpenI-IU-CXR/`.
