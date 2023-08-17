# 1. import
import win32com.client



# 2. 엑셀 Application 열기
# 엑셀 프로그램 실행
excel = win32com.client.Dispatch("Excel.Application")

# 앞으로 실행과정을 보이게 함
excel.Visible = True



# 3. Workbook 및 Worksheet 객체 생성
# 엑셀 프로그램에 Workbook 추가(객체 설정)
wb = excel.Workbooks.Add()
# Worksheet 설정
# 즉 엑셀 '통합문서'가 만들어지면서 'Sheet1'을 생성하는 방법.
ws = wb.Worksheets("sheet1")


# 원래 있는 엑셀 파일을 Workbook 객체로 생성하는 방법
# wb = excel.Workbooks.Open(r"경로")


# 4. Cell에 데이터 써보기
# 셀 row, col 값 지정하여 값 넣기(Range("A1")과 동일함)
ws.cells(1,1).Value = "win32com excel test1"

# range로 값 넣기(Cell(1, 2)와 동일함)
ws.Rang("A2").Value = "win32com excel test2"

# range로 다중범위 지정해서 값 넣기1
ws.Range("A3:C3").Value = "win32com excel test3"

# range로 다중범위 지정해서 값 넣기2(위 코드와 동일 표현)
ws.Range(ws.Cells(3, 1), ws.Cells(3,3)).Value = "win32com excel test3"

# 엑셀의 자동 채우기 기능 활용
ws.Range('A1:A3').AutoFill(ws.Range("A1:A10"))



# 5. Cell data 복사/붙여넣기
# "A1:A10" 데이터 복사하기
ws.Range("A1:A10").Copy()
# 붙여넣기할 위치 선택
ws.Range("B1").Select()
# 붙여넣기 실행
ws.Paste()


# 6. 파일 저장하기
# 파일 저장
wb.Save()
# 다른 이름으로 파일 저장
wb.SaveAs(r"경로\파일명")



# 7. 엑셀 Application 닫기
excel.Quit()
