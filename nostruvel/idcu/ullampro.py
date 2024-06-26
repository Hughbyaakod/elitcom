import openpyxl

# Load the Excel workbook
workbook = openpyxl.load_workbook('your_file.xlsx')

# Iterate through all the sheet names
for sheet_name in workbook.sheet_names:
    print(sheet_name)
