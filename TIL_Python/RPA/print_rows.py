import openpyxl as op

wb = op.load_workbook("test.xlsx")
ws = wb["업"]

print("#rows 출력")
for row_rng in ws.rows:
    print(row_rng)