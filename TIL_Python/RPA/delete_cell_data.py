import openpyxl as op

wb = op.load_workbook("result2.xlsx")
ws = wb["업"]

rng = ws["A1:C3"]

# 튜플에 대한 for 문
for row_data in rng:
    for data in row_data:
        # 해당 data가 2로 나눈 나머지가 0이면 공백처리
        if (data.value % 2) == 0:
            data.value = ""

wb.save("delete_result.xlsx")