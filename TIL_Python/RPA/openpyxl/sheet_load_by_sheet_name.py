import openpyxl as op

wb = op.load_workbook(r"test.xlsx")

print(wb)

ws = wb["무"]

print(ws)