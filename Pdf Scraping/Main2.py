import PyPDF2
import pandas as pd

with open("sample2.pdf", "rb") as pdf_file:
    read_pdf = PyPDF2.PdfReader(pdf_file)
    number_of_pages = len(read_pdf.pages)
    page = read_pdf.pages[0]
    page_content = page.extract_text().splitlines()
    name = ""
    address = ""
    account_no = ""
    date = ""
    date_2 = []
    due_date = ""
    new_balance = ""
    minimum_balance = ""

    for line in page_content:
        if "Name" in line:
            parts = line.split(': ')
            name = parts[-1]
        if "Address" in line:
            parts = line.split(': ')
            if "Address" in line and "Account Number" in line:
                address = line.split("Address: ")[1].split("Account Number")[0].strip()
                account_no = line.split("Account Number: ")[1].split("For Lost")[0].strip()
        if "Date" in line:
            parts = line.split(': ')
            date = parts[-1].split()[0]
            date_2.append(date)
            print(date_2)
#         elif "Payment Due Date" in line:
#             parts = line.split(' ')
#             due_date = parts[-1]
#         elif "New Balance" in line:
#             parts = line.split(' ')
#             new_balance = parts[-1]
#         elif "Minimum Payment" in line:
#             parts = line.split(' ')
#             minimum_balance = parts[-1]
#
# # Create a list of dictionaries with the extracted values
# data = [{"Name": name,"Address": address, "Account Number": account_no,"Payment Due Date": date, "New Balance": new_balance, "Minimum Payment": minimum_balance}]
#
# # Create a DataFrame from the list of dictionaries
# df = pd.DataFrame(data)
#
# # Print the DataFrame
# print(df)
#
# # Save the DataFrame to a CSV file
# df.to_csv("PdfExtraction2.csv", index=False)
