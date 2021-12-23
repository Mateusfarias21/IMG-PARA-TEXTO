import abc
import cv2
import pytesseract

#Transformando Imagem em Texto

img = cv2.imread("teste02.jpg")

pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\Tesseract.exe"

resultado = pytesseract.image_to_string(img)

print(resultado)






