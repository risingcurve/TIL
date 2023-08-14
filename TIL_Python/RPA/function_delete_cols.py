import openpyxl as op

wb = op.load_workbook("delete_test.xlsx")
ws = wb.active

# 2열부터 1개열까지 열을 삭제한다.
ws.delete_cols(2,1)

wb.save("delete_cols_result.xlsx")