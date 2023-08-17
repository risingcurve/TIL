# win32 통해 엑셀 다루기 - Cell 영역을 선택하는 방법

# import 및 Workbook, Worksheet 객체 설정
import win32com.client

excel = win32com.client.Dispatch("Excel.Application") #엑셀 프로그램 실행

excel.Visible = True  #앞으로 실행과정을 보이게

wb = excel.Workbooks.Open("test.xlsx") #기존에 생성된 문서를 Workbook 객체로 생성
ws = wb.ActiveSheet #활성화 된 시트 "Sheet1"을 객체로 생성


# 1. Range
# "a1" 영역을 선택
ws.Range("A1").Select() 

# "A1", "B2" 영역을 각 각 선택
ws.Range("A1,B2").Select() 

# "A2:B3"의 연속 된 영역 선택
ws.Range("A2:B3").Select() 


# 특정 영역 값 출력
# "A2:B3"의 연속된 영역 선택
ws.Range("A2:B3").value

# 결과
# ((pywintypes.datetime(2021, 6, 8, 0, 0, tzinfo=TimeZoneInfo('GMT Standard Time', True)), '식비'), (pywintypes.datetime(2021, 6, 8, 0, 0, tzinfo=TimeZoneInfo('GMT Standard Time', True)), '식비'))



# 2. UsedRange

# 사용 영역 출력해 보기
ws.UsedRange()

# 결과
#(('text1', 'text2', 'text3'), ('text4', None, 'text5'), (None, 'text6', None))


# 사용 영역 출력해보기  
print("A1 값 :", ws.UsedRange()[0][1])
print("B3 값 :", ws.UsedRange()[1][2])

# 결과
# # A1 값 : text2 
# B3 값 : text5


# 해당 영역을 직접 엑셀에서 선택 처리 : UsedRange 뒤에 Select( ) 함수를 사용하면 실제 영역을 선택
# 사용 영역 선택처리하기
# UsedRange는 위 결과처럼 시트의 연속 된 사용 영역을 모두 선택 처리. data가 입력되어있는 것 뿐만 아니라 셀 서식이 적용되어있거나 셀의 행/열 높이가 수정 된 경우에도 사용 영역으로 인식.
ws.UsedRange.Select()



# 3. CurrentRegion

# UsedRange는 앞에 대상이 되는 객체가 WorkSheet(=ws)인 것에 반해 CurrentRegion의 대상이 되는 객체는 Range.
# A:C 열의 사용 영역 선택하기
ws.Range("A:C").CurrentRegion.Select()

# 시트 사용 영역 선택하기
ws.UsedRange.CurrentRegion.Select()

