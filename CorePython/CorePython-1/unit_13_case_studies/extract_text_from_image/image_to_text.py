import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
text1 = pytesseract.image_to_string(r'image_1.JPG')
file1 = open("text.txt","w")
file1.write(text1)
