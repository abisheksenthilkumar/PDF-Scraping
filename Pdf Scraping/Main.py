import os
import pdf2image
from PIL import Image
import pytesseract
import openpyxl

# Set the path to Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_pdf(pdf_path):
    images = pdf2image.convert_from_path(pdf_path)
    text = ""
    for i, image in enumerate(images):
        text += pytesseract.image_to_string(image)
    return text

def save_to_excel(text, excel_path):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet['A1'] = "Extracted Text"
    sheet['A2'] = text

    workbook.save(excel_path)

pdf_path = r'C:\Users\abish\Documents\SRM Intern\Pdf Scraping\sample.pdf'
excel_path = r'C:\Users\abish\Documents\SRM Intern\Pdf Scraping\output.xlsx'

text = extract_text_from_pdf(pdf_path)
save_to_excel(text, excel_path)
