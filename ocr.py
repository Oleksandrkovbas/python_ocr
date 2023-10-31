from PIL import Image
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

filename = 'passport.jpg'
print(pytesseract.image_to_string(Image.open(filename)))
