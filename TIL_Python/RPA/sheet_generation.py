import openpyxl as op

wb = op.Workbook()

ws = wb.create_sheet("new_sheet")

print(ws)

wb.save("test_result.xlsx")