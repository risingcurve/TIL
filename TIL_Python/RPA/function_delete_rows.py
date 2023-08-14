import openpyxl as op

wb = op.load_workbook("delete_test.xlsx")
ws = wb.active

# 1행부터 2개행까지 행을 삭제한다.
ws.delete_rows(1,2)

wb.save("delete_rows_result.xlsx")