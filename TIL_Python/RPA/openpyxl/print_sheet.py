import openpyxl as op

wb = op.load_workbook(r"test.xlsx")

ws_list = wb.sheetnames

for sht in ws_list:
    ws = wb[sht]
    print(ws)