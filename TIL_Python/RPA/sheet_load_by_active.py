import openpyxl as op

wb = op.load_workbook(r"test.xlsx")

ws = wb.active

print(ws)