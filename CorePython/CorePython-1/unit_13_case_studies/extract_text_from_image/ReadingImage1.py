# pip install pytesseract
# dowmload and install tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe from https://github.com/UB-Mannheim/tesseract/wiki
# pip install opencv-python

import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
path1 = 'D:/KrishnaAryal/Training2020/JavaScript/javascript-1/dom_bom2.PNG'
path2 = 'C:\\Users\\Krishna\\Google Drive\\PBS\\BScIT\\Summer-5 2021\\SectionC\\June7\\3.png'
text = pytesseract.image_to_string(path1)
print(text)