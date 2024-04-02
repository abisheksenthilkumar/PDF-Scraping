import fitz
import csv
import re

def extract_features_from_text(text):
    features = {
        'Invoice Number': None,
        'Order Number': None,
        'Invoice Date': None,
        'Due Date': None,
        'Total Due': None,
        'To': None,
        'ACC #': None,
        'BSB #': None,
        'Paid': None
    }

    for key in features.keys():
        match = re.search(rf'{key}[\s:]+(.+?)(?=\n|$)', text)
        if match:
            features[key] = match.group(1)

    return features

def pdf_to_csv(pdf_file, csv_file):
    # Open the PDF file
    doc = fitz.open(pdf_file)

    # Open CSV file for writing
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Invoice Number', 'Order Number', 'Invoice Date', 'Due Date', 'Total Due', 'To', 'ACC #', 'BSB #', 'Paid']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()

        # Iterate through each page of the PDF
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text = page.get_text()

            # Extract features from the text
            features = extract_features_from_text(text)

            # Write features to CSV
            csv_writer.writerow(features)

    doc.close()

# Example usage
pdf_file = "C:/Users/abish/Documents/SRM Intern/Pdf Scraping/sample.pdf"  # Provide the path to your PDF file here
csv_file = "output.csv"  # Provide the desired CSV output file name here
pdf_to_csv(pdf_file, csv_file)
def display_csv(csv_file):
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            print(' '.join(row))

# Example usage
csv_file = "output.csv"  # Provide the path to your CSV file here
display_csv(csv_file)