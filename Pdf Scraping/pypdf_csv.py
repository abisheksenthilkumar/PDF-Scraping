import PyPDF2
import pandas as pd

with open("sample.pdf", "rb") as pdf_file:
    read_pdf = PyPDF2.PdfReader(pdf_file)
    number_of_pages = len(read_pdf.pages)
    page = read_pdf.pages[0]
    page_content = page.extract_text().splitlines()
    invoice_no = ""
    order_no = ""
    date = ""
    date2 = ""
    amount = ""

    for line in page_content:
        if "Invoice Number" in line:
            parts = line.split(' ')
            invoice_no = parts[-1]
        if "Order Number" in line:
            parts = line.split(' ')
            order_no = parts[-1]
        elif "Invoice Date" in line:
            parts = line.split(' ')
            date = ' '.join(parts[-3:])
        elif "Due Date" in line:
            parts = line.split(' ')
            date2 = ' '.join(parts[-3:])

        elif "Total Due" in line:
            parts = line.split(' ')
            amount = parts[-1]

# Create a list of dictionaries with the extracted values
data = [{"Invoice Number": invoice_no,"Order Number": order_no, "Invoice Date": date,"Due Date": date2, "Total Due": amount}]

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

# Save the DataFrame to a CSV file
df.to_csv("PdfExtraction.csv", index=False)
