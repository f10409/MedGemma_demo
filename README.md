# MedGemma Demo
Zero-shot and few-shot prompting for medical image classification with MedGemma.

**Frank Li** | HITI Lab, Emory University | Datathon 2025

## Usage
```bash
cd ~
git clone https://github.com/f10409/MedGemma_demo.git
```
Launch Jupyter and select the `medsiglip` kernel to run the demo.

## Installation
If the pre-installed environment doesn't work:
```bash
cd ~/MedGemma_demo
conda deactivate
uv sync
source .venv/bin/activate
python -m ipykernel install --user --name medgemma
```
Launch Jupyter and select the `medgemma` kernel to run the demo.