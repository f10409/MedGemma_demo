import os
import urllib.request
import zipfile

from utils.openi_data import OPENI_URL

MONTGOMERY_ZIP = "NLM-MontgomeryCXRSet.zip"


def download_montgomery(dest="data/Montgomery-CXR"):
    """
    Download the Montgomery County chest X-ray set from NLM: 138 images with lung masks.

    Makes the folder layout that RadHarmony expects: dest/MontgomerySet/CXR_png,
    ManualMask (leftMask, rightMask), and ClinicalReadings. Skips the download if it is done.

    Args:
        dest: Output folder.

    Returns:
        str: The image folder (dest/MontgomerySet/CXR_png).
    """
    image_dir = os.path.join(dest, "MontgomerySet", "CXR_png")
    done = os.path.join(dest, f".{MONTGOMERY_ZIP}.done")  # Written only after a full extraction
    if not os.path.exists(done):
        os.makedirs(dest, exist_ok=True)
        zip_path = os.path.join(dest, MONTGOMERY_ZIP)
        print(f"⬇️  Downloading {MONTGOMERY_ZIP} ...")
        urllib.request.urlretrieve(f"{OPENI_URL}/{MONTGOMERY_ZIP}", zip_path)
        print(f"📦 Extracting {MONTGOMERY_ZIP} ...")
        with zipfile.ZipFile(zip_path) as z:
            # Skip the macOS files (__MACOSX/) in the archive
            z.extractall(dest, [m for m in z.namelist() if m.startswith("MontgomerySet/")])
        os.remove(zip_path)
        if not os.path.isdir(image_dir) or not any(f.endswith(".png") for f in os.listdir(image_dir)):
            raise RuntimeError(f"No images in {image_dir} after the extraction. The archive layout changed.")
        open(done, "w").close()
    print(f"✅ Montgomery data ready: {image_dir}")
    return image_dir
