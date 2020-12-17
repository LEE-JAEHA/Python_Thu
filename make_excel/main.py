import xlsxwriter
from openpyxl import load_workbook
workbook = xlsxwriter.Workbook("./test.xlsx")
worksheet = workbook.add_worksheet("test")
#default는 sheet1

worksheet.write("A1","Hello workd")
worksheet.write(2,1,"TEST")

workbook.close()