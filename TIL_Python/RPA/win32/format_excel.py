'''
이번 파트에서는 win32com.client를 통해 엑셀 셀서식을 설정하는 방법을 알아보겠습니다. 셀서식 파트의 내용은 아래와 같은 순서도 다뤄보겠습니다.

1. Font Style
2. Font Color(글 색상)
3. Cell 서식 : 색상, 테두리, 정렬
4. Font, Cell 서식 지우기
'''

import win32com.client

excel = win32com.client.Dispatch("Excel.Application") #엑셀 프로그램 실행
excel.Visible = True #앞으로 실행과정을 보이게

wb = excel.Workbooks.Add() #엑셀 Workbook 파일 1개 새로 생성
ws = wb.Worksheets.Add() #엑셀 시트를 새로 생성


# 1. Font Style

#다중범위 써보기1
ws.Range(ws.cells(1,1), ws.cells(1,3)).value = "win32com excel 서식(font style)"

#다중범위 써보기2
ws.Range("A2:B2").value = "win32com excel 서식(font 색상)"

#다중범위 써보기3
ws.Range("A3").value = "win32com excel 서식(Cell 색상)"


#셀서식1. font size 및 font 굵게, 글씨체

#"A1" 글씨체 변경
ws.cells(1,1).Font.name = "굴림"

#"B2"글씨 사이즈 변경
ws.cells(1,2).Font.Size = 14 

#"C3"글씨 스타일 변경(Bold, Italic, Underline)
ws.cells(1,3).Font.Bold = True #굵게
ws.cells(1,3).Font.italic = True #글씨 기울기
ws.cells(1,3).Font.Underline = True #밑줄


# 2. Font Color

#셀서식2. font 색상 지정
ws.Range("A2").font.ColorIndex = 40
ws.Range("B2").font.ColorIndex = 50



# 3. Cell 서식 : 색상, 테두리, 정렬

# 1) Cell 색상
#"A3" 셀 배경색 지정
ws.Range("A3").Interior.ColorIndex = 30

# 2) Cell 테두리 지정
#Weight : 선 굵기, LineStyle의 경우 1:실선, 2:짧은점선, 3:긴점선 
ws.Range("A1:C3").BorderAround(ColorIndex = 1,Weight = 2,LineStyle = 1)

#셀 안쪽까지 모두 테두리 지정
rng = ws.Range("A1:C3") #범위 설정
rng.Borders.LineStyle = 1 #선 스타일
rng.Borders.ColorIndex = 14 #선 색상
rng.Borders.Weight = 2 #선 굵기

# 3) Cell 정렬
#행, 열크기 조정
rng = ws.UsedRange # 사용 영역 선택
rng.rowHeight = 70  # 선택 영역 행 크기 설정
rng.ColumnWidth = 30  # 선택 영역 열 크기 설정

#테두리 설정
rng.Borders.LineStyle = 1 #선 스타일
rng.Borders.ColorIndex = 1 #선 색상 : Black
rng.Borders.Weight = 2 #선 굵기


#B1
ws.Range("B1").VerticalAlignment = -4160  #위로 정렬
ws.Range("B1").HorizontalAlignment = -4108  #가운데 정렬(수평)

#B3
ws.Range("B3").VerticalAlignment = -4107  #아래로 정렬
ws.Range("B3").HorizontalAlignment = -4108  #가운데 정렬(수평)

#A2
ws.Range("A2").VerticalAlignment = -4108  #가운데 정렬(수직)
ws.Range("A2").HorizontalAlignment = -4131  #왼쪽으로 정렬

#C2
ws.Range("C2").VerticalAlignment = -4108  #가운데 정렬(수직)
ws.Range("C2").HorizontalAlignment = -4152  #오른쪽으로 정렬

#B2
ws.Range("B2").VerticalAlignment = -4108  #가운데 정렬(수직)
ws.Range("B2").HorizontalAlignment = -4108  #가운데 정렬(수평)


# 4. Font, Cell 서식 지우기
#폰트, 셀서식 초기화(ClearContents일 겨우 내용만 삭제, Clear는 내용,서식 모두 초기화)
ws.Range("A1:C3").ClearFormats()
