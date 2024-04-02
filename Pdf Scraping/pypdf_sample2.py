import re
import csv
from PyPDF2 import PdfReader

def extract_rates(text):
    rates = {}

    pattern_periodic_rate = r'Periodic Rate\s+(\d+\.\d+)%\s+(\d+\.\d+)%'
    pattern_apr = r'Annual Percentage Rate \(APR\)\s+(\d+\.\d+)%\s+(\d+\.\d+)%'

    match_periodic_rate = re.search(pattern_periodic_rate, text)
    if match_periodic_rate:
        rates['Periodic Rate'] = (float(match_periodic_rate.group(1)), float(match_periodic_rate.group(2)))

    match_apr = re.search(pattern_apr, text)
    if match_apr:
        rates['Annual Percentage Rate (APR)'] = (float(match_apr.group(1)), float(match_apr.group(2)))

    return rates

def extract_features_from_pdf(pdf_file):
    features = {
        'Name': None,
        'Address': None,
        'Account Number': None,
        'Date': None,
        'Payment Due Date': None,
        'New Balance': None,
        'Minimum Payment': None,
        'Previous Balance': None,
        'Payment, Credits': None,
        'Purchases': None,
        'Cash Advances': None,
        'Balance Transfers': None,
        'Fees Charged': None,
        'Interest Charged': None,
        'Payment Due Date': None,
        'Minimum Payment Due': None,
        'Opening/Closing Date': None,
        'Credit Access Line': None,
        'Available Credit': None,
        'Cash Access Line': None,
        'Available for Cash': None,
        'Past Due Amount': None,
        'Balance Over the Credit Access Line': None,
        'Periodic Rate': None,
        'Annual Percentage Rate (APR)': None
    }

    pdf = PdfReader(pdf_file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()

    for key in features.keys():
        match = re.search(rf'{key}:?\s+(.+?)(?=\n|$)', text)
        if match:
            features[key] = match.group(1)

    rates = extract_rates(text)
    for key, value in rates.items():
        features[key] = value

    return features

def write_features_to_csv(features, csv_file):
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = list(features.keys())
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerow(features)

def display_csv(csv_file):
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            for key, value in row.items():
                print(f"{key}: {value}")
            print()

pdf_file = "C:/Users/abish/Documents/SRM Intern/Pdf Scraping/sample2.pdf"
csv_file = "C:/Users/abish/Documents/SRM Intern/Pdf Scraping/output2.csv"

features = extract_features_from_pdf(pdf_file)

write_features_to_csv(features, csv_file)

display_csv(csv_file)