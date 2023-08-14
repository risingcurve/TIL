import openpyxl as op

# 워크북 객체 생성(파일명 : test.xlsx)
wb = op.load_workbook(r"test.xlsx")

# 활성화 되어있는 시트 설정(시트명 : "업")
ws = wb.active

# 방법 1 : Sheet의 Cell 속성 사용하기
data1 = ws.cell(row = 1, column = 2).value

# 방법 2 : 엑셀 인덱스(Range) 사용하기
data2 = ws["B1"].value

# 위 결과 출력
print("cell(1, 2) : ", data1)
print('Range("B1") : ', data2)

# .value 없이 접근하면 튜플로 출력
data3 = ws.cell(row = 1, column = 2)
data4 = ws["B1"]
print(data3)
print(data4)

# cell에 range로 접근하기
# A1:B1 범위 저장
rng = ws["A1:B1"]

# 출력값은 튜플
print("Range(a1:b1) : ", rng)

# A1:C3 범위 저장(총 9개 cell)
rng2 = ws["A1:C3"]

# 결과 출력(튜플)
# 출력 결과 이차원 튜플
print(rng2)

# 튜플의 첫번째 차원 : 각 행
for rng2_data in rng2:
    # 튜플의 두번째 차원을 위한 for 문 : 1개의 cell 요소
    for cell_data in rng2_data:
        # 각 cell 요소의 값 출력
        print(cell_data.value)