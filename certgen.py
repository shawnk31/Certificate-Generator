from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

# Paths
TEMPLATE_PATH = r"D:\Certimg\Template.png"
EXCEL_PATH = r"D:\Certimg\data.xlsx"
OUTPUT_DIR = r"D:\Certimg\Output"

# Create output directory if not exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load Excel data without header
df = pd.read_excel(EXCEL_PATH, header=None)

# Load template image once
template = Image.open(TEMPLATE_PATH)
width, height = template.size

# Load font
font_path = r"C:\Users\shash\Downloads\glacial-indifference\GlacialIndifference-Bold.otf"
name_font = ImageFont.truetype(font_path, size=60)

# Text Y-position (adjust if needed)
NAME_POSITION_Y = 580

# Generate certificates
for index, row in df.iterrows():
    name = str(row[0]).upper()

    cert = template.copy()
    draw = ImageDraw.Draw(cert)

    bbox = draw.textbbox((0, 0), name, font=name_font)
    name_width = bbox[2] - bbox[0]
    name_position = ((width - name_width) // 2, NAME_POSITION_Y)

    draw.text(name_position, name, fill="black", font=name_font)

    # Output filename (clean, lowercase, no spaces)
    filename = f"{name.lower().replace(' ', '_').replace('.', '')}.jpg"
    output_path = os.path.join(OUTPUT_DIR, filename)

    cert.convert("RGB").save(output_path)

print("✅ Certificates generated successfully!")
