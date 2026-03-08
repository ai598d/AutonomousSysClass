import subprocess
import os

# ------------- CONFIG ----------------
mht_file = r"C:\Users\ai598\Documents\WINTER 2026\Git\Lecture5.mht"
output_dir = r"C:\Users\ai598\Documents\WINTER 2026\Git\Lecture5_html"
libreoffice_path = r"C:\Program Files\LibreOffice\program\soffice.exe"
# --------------------------------------

# Create output folder if it does not exist
os.makedirs(output_dir, exist_ok=True)

# Run LibreOffice headless conversion
subprocess.run([
    libreoffice_path,
    "--headless",
    "--convert-to", "html",
    mht_file,
    "--outdir", output_dir
])

print(f"✅ Conversion complete! HTML + resources saved in '{output_dir}'")