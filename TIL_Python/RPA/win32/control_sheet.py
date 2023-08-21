'''
이번 파트는 win32com.cleint 모듈을 사용하여 엑셀 시트를 다루는법을 알아보겠습니다. 서론에서 win32com.client가 엑셀의 기능적인 측면에서 OpenPyxl보다 더 편리하다라고 언급한 적이 있습니다.

예를 들어, win32com.client로 엑셀 시트를 제어하면 여러 엑셀 파일간 시트 이동/복사가 가능해집니다. (OpenPyxl에서는 불가능한 작업입니다.)

아래 5가지 부분으로 나누어 설명해보도록 하겠습니다.
'''

# 1. 시트 생성 및 설정

# win32com.client 모듈 임포트
import win32com.client

# Excel 프로그램 객체 생성
excel=win32com.client.Dispatch("Excel.Application")

# 엑셀 실행과정이 보이게 설정
excel.Visible = True


#기존에 있는 "data1.xlsx"파일을 Workbook 객체로 설정
wb1 = excel.Workbooks.Open(r"C:경로\data1.xlsx")



# 2. 시트 복사 및 이동

#data1.xlsx 파일에 새로운 Worksheet 생성 및 ws1으로 객체 설정
ws1 = wb1.Worksheets.Add()

#data1.xlsx 파일에 새로운 Worksheet 생성 및 ws2으로 객체 설정
ws2 = wb1.Worksheets.Add()

#현재 활성화되어 있는 시트를 객체로 설정(위 이미지 기준 Sheet2)
ws3 = wb1.ActiveSheet

#특정 시트명으로 접근(Sheet1으로 접근)
ws4 = wb1.Worksheets("sheet1")

#"data1.xlsx" 파일을 wb1로 설정
wb1 = excel.Workbooks.Open(r"C:\Users\Desktop\VS CODE\Project\17. win32com\data1.xlsx")

#"data2.xlsx" 파일을 wb2로 설정
wb2 = excel.Workbooks.Open(r"C:\Users\Desktop\VS CODE\Project\17. win32com\data2.xlsx")

#wb1의 "test" 시트를 wb2의 "Sheet1" 앞으로 복사한다.
wb1.Worksheets("test").Copy(Before=wb2.Worksheets("Sheet1"))



# 3. 시트삭제

wb = excel.Workbooks.Add() #엑셀 Workbook 파일 1개 새로 생성

ws = wb.Worksheets.Add() #엑셀 시트를 새로 생성

#"Sheet1"을 ws로 설정
ws = wb.Worksheets("Sheet1")
#ws 삭제
ws.Delete()

#"Sheet1" 삭제하기
wb.Worksheets("Sheet1").Delete()



# 4. 시트 속성 설정(시트명, 시트탭 색)

#"Sheet2"을 ws로 설정
ws = wb.Worksheets("Sheet2")
#ws 시트명 바꾸기
ws.Name = "시트 이름 바꾸기"

# Microsoft에서 제공하는 엑셀 ColorIndex는 1~56이며, 각 번호가 뜻하는 색상은 Excel Color Index 검색
ws.Tab.ColorIndex = 30


