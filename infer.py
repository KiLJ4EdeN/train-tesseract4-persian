import sys
import pytesseract

try:
    from PIL import Image
except ImportError:
    import Image


lang = sys.argv[1]
img_path = sys.argv[2]

img = Image.open(img_path)
custom_psm_config = r'--psm 8'
raw_text = pytesseract.image_to_string(img, lang=lang, config=custom_psm_config)
with open('out.txt', 'w') as f:
    f.write(raw_text)
