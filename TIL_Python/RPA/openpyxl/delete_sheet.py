import openpyxl as op

wb = op.load_workbook("delete_sheet.xlsx")

# 'test'라는 이름을 가진 sheet를 객체로 생성
ws = wb['test']

# test 시트 삭제
wb.remove(ws)

# test 시트 재생성
wb.create_sheet('test')

wb.save("delete_sheet_result.xlsx")