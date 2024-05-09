import sys
import pytesseract
from difflib import SequenceMatcher as SQ

try:
    from PIL import Image
except ImportError:
    import Image


lang = sys.argv[1]

img_path = 'data/validation/8000.png'
img = Image.open(img_path)
raw_text = pytesseract.image_to_string(img, lang=lang)  # make sure to change your `config` if different 
print(f'output: {raw_text}')
