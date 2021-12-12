#IMP URLs: 
# http://zetcode.com/python/openpyxl/
# https://realpython.com/openpyxl-excel-spreadsheets-python/
# https://www.freecodecamp.org/news/how-to-create-read-update-and-search-through-excel-files-using-python-c70680d811d4/
# Styling Excel sheet : https://openpyxl.readthedocs.io/en/stable/styles.html


# (1)    Append data to existng EXCEl SHEET ....
from openpyxl import load_workbook
workbook = load_workbook(filename="hello_world.xlsx")
sheet = workbook.active
data = [(99,99),(111,111),(3333,333),(444,444)]
for row in data:
    sheet.append(row)
workbook.save(filename="hello_world.xlsx")





