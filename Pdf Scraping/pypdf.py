import PyPDF2

with open("sample.pdf", "rb") as pdf_file:
    read_pdf = PyPDF2.PdfReader(pdf_file)
    number_of_pages = len(read_pdf.pages)
    page = read_pdf.pages[0]
    page_content = page.extract_text().splitlines()
    invoice_no = ""
    date = ""
    amount = ""

    for line in page_content:
        # print("Processing Line:", line)
        if "Invoice Number" in line:
            parts = line.split(' ')
            print(parts[-1])
            invoice_no= parts[-1]
            if len(parts) > 1:
                invoice_no = parts[1].strip()
        elif "Invoice Date" in line:
            parts = line.split(' ')
            date=' '.join(parts[-3:])
            print(date)
        elif "Total Due" in line:
            parts = line.split(' ')
            print(parts[-1])
            amount=parts[-1]
