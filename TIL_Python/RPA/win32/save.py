'''
이번 파트에서는 win32com.client를 통해 엑셀 파일을 저장하는 여러가지 방법에 대해 알아보겠습니다. 엑셀 업무자동화에서 중요한 부분 중 하나는 원하는 파일을 사용자가 원하는 형태로 저장하는 것입니다. 사용자에 따라 엑셀 파일을 필요한 시트만 저장하거나, pdf 파일 등 다른 형식의 파일로 저장해야하는 경우도 생깁니다. 아래 내용을 공부하시면 저장 방법에 대한 기초적인 내용을 아실 수 있습니다.

아래와 같은 3가지 함수를 배워보겠습니다.
'''

# 1. Save()

# Save 함수는 별다른 설정 옵션 없이 "통합문서"라는 이름으로 파일을 저장합니다. Save 함수를 사용해보기 전에 먼저 임의의 Workbook 객체를 생성하는 코드를 작성해보겠습니다.

import win32com.client

#excel App 열기(객체 생성)
excel = win32com.client.Dispatch("Excel.Application")

#엑셀 실행과정이 보이게
excel.Visible = True

#Workbook 객체 생성(새로 추가)
wb = excel.Workbooks.Add()

#Workbook(통합문서) 저장
wb.Save() 



# 2. SaveAs()

# 기본 사용법
"Workbook 객체".SaveAs("파일명, 파일포맷, 비밀번호...")  

#path 지정
path = r"C:\Users\Desktop\VS CODE\Project\17. win32com\결과"

#저장
wb.SaveAs(path+"/test1.xlsx")



# 3. ExportAsFixedFormat()

# 특정 엑셀 시트를 .pdf 파일과 같이 원하는 확장자로 추출
"WorkSheet 객체".ExportAsFixedFormat("Type", "FileName", "From", "To")  

# 1) Type
# Type은 추출할 형식을 선택합니다. 0을 입력할시 pdf 형식, 1을 입력할시 xps 형식으로 파일을 추출합니다. 해당 내용은 Microsoft 공식 문서에도 나와있습니다.

# 2) FileName
# 이 부분은 SaveAs 함수에서 배웠던 내용과 동일합니다. 경로 및 파일명을 지정할 수 있습니다.

# 3) From, To
# From은 해당 엑셀 시트에서 저장할 시작 페이지를 의미합니다. To는 해당 엑셀 시트에서 저장할 마지막 페이지입니다.

# 예시 코드
#모듈 임포트
import  win32com.client

#excel 객체 생성 및 실행과정 보이게
excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True

#신규 엑셀 문서 생성
wb = excel.Workbooks.Add()
#활성화 된 시트를 ws로 설정
ws = wb.ActiveSheet

# 1행 1열에 텍스트 입력
ws.cells(1,1).Value = "사장님 몰래 하는 파이썬 업무자동화"

#저장할 경로 설정
path = r"C:\Users\Desktop\VS CODE\Project\17. win32com\결과" 

#pdf 파일로 저장하기 (1 page)
ws.ExportAsFixedFormat(Type=0, Filename=path+"/test.pdf",From=1,To=1)  


