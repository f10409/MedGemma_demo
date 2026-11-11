# MedGemma Demo
Chest X-ray visual question answering (VQA) and classification, radiology report generation, and anatomy localization with MedGemma 1.5 (`google/medgemma-1.5-4b-it`). Zero-shot classification, linear probing, and segmentation with MedSigLIP (`google/medsiglip-448`). MedGemma uses the image encoder of MedSigLIP.

**Frank Li, Judy Gichoya, Mohammadreza Chavoshi** | HITI Lab, Emory University | RSNA 2026 Deep Learning Lab

## Notebooks
| Notebook | What it does | Colab |
|---|---|---|
| `1_medgemma_demo.ipynb` | Data download, Hugging Face access, VQA and classification, report generation, anatomy localization, web app | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/f10409/MedGemma_demo/blob/main/1_medgemma_demo.ipynb) |
| `2_medsiglip_demo.ipynb` | MedSigLIP image encoder with RadHarmony evaluators: zero-shot classification, linear probing, lung segmentation | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/f10409/MedGemma_demo/blob/main/2_medsiglip_demo.ipynb) |

## Before the Session
Complete **Step 2 in notebook 1** before the session. In this step, you accept the MedGemma 1.5 terms, make a Hugging Face token, and save it in Colab. Also accept the terms on the [MedSigLIP page](https://huggingface.co/google/medsiglip-448) for notebook 2.

## Usage (Google Colab)
1. Open a notebook in Colab. Select **Runtime → Change runtime type → T4 GPU**.
2. Run the first code cell. It gets the helper code and downloads the data. While it runs, accept the model terms (MedGemma 1.5 for notebook 1, MedSigLIP for notebook 2) and save your Hugging Face token as the `HF_TOKEN` secret (Step 2 in the notebook).
3. Run the other cells. The setup cell installs [RadHarmony](https://github.com/f10409/RadHarmony) and checks your access. When Colab asks for access to the `HF_TOKEN` secret, click **Grant access**.

## Data
Both notebooks use the open-access [Open-i Indiana University chest X-ray collection](https://openi.nlm.nih.gov/faq) (3,955 reports, 7,470 images). The notebooks download it (about 1.4 GB) and load it with RadHarmony (`OpenICXRHarmonizer`, `OpenICXRDataset`).

Notebook 2 also uses the [Montgomery County chest X-ray set](https://data.lhncbc.nlm.nih.gov/public/Tuberculosis-Chest-X-ray-Datasets/Montgomery-County-CXR-Set/MontgomerySet/index.html) (138 images with lung masks) for segmentation. The notebook downloads it (about 0.6 GB) and loads it with RadHarmony (`MontgomeryCXRDataset`).

Citations:
- Demner-Fushman D, et al. Preparing a collection of radiology examinations for distribution and retrieval. *JAMIA*. 2016;23(2):304–310.
- Jaeger S, et al. Two public chest X-ray datasets for computer-aided screening of pulmonary diseases. *Quant Imaging Med Surg*. 2014;4(6):475–477.
- Candemir S, et al. Lung segmentation in chest radiographs using anatomical atlases with nonrigid registration. *IEEE Trans Med Imaging*. 2014;33(2):577–590.

## Local Installation
```bash
git clone https://github.com/f10409/MedGemma_demo.git
cd MedGemma_demo
uv sync
source .venv/bin/activate
python -m ipykernel install --user --name medgemma
```
Log in to Hugging Face with `hf auth login`. Then launch Jupyter and select the `medgemma` kernel. The data downloads to `data/`.
