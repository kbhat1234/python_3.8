# Import the xlrd module
import xlrd as xl

# Define the location of the file
loc = "C://ab.xlsx"

# To open the Workbook
wb = xl.open_workbook(loc)
sheet = wb.sheet_by_index(0)


# For row 0 and column 0
print(sheet.cell_value(0, 0))
print(sheet.cell_value(1, 0))