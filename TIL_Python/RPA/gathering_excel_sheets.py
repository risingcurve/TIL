'''
개별 파일의 엑셀 시트 새 파일에 취합하기
1. 프로그램 컨셉
오늘은 제목과 같이 개별 엑셀 파일의 특정 시트들을 새로운 엑셀 파일에 모두 합치는 파이썬 프로그램을 만들어 보겠습니다.

수십 수백개의 엑셀 파일의 특정 시트들을 보고싶거나 인쇄할 때 한곳으로 취합한다면 훨씬 시간을 절약할 수 있겠죠?

대략적인 컨셉은 다음과 같습니다.



2. 사용 라이브러리 정보
Pywin32 (엑셀 어플리케이션을 다루기 위함)
glob (폴더 내의 엑셀 파일의 경로를 가져오기 위함)
'''


# step1.관련 모듈 및 패키지 import
import glob
import win32com.client

# step2.win32com(pywin32)를 이용해서 엑셀 어플리케이션 열기
excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True #실제 작동하는 것을 보고 싶을 때 사용

# step3.엑셀 어플리케이션에 새로운 Workbook 추가
wb_new = excel.Workbooks.Add() 

# step4.glob 모듈로 원하는 폴더 내의 모든 xlsx 파일의 경로를 리스트로 반환
list_filepath = glob.glob(r'C:\Users\SANGWOO\Desktop\VSCODE\엑셀 샘플\*.xlsx', recursive=True)

# step5.엑셀 시트를 추출하고 새로운 엑셀에 붙여넣는 반복문
for filepath in list_filepath:

    # 받아온 엑셀 파일의 경로를 이용해 엑셀 파일 열기
    wb = excel.Workbooks.Open(filepath)

    # 새로 만든 엑셀 파일에 추가
    # 추출할wb.Worksheets("추출할 시트명").Copy(Before=붙여넣을 wb.Worksheets("기준 시트명")
    wb.Worksheets("코딩유치원").Copy(Before=wb_new.Worksheets("Sheet1"))

# step6. 취합한 엑셀 파일을 "통합 문서"라는 이름으로 저장
wb_new.SaveAs(r"C:\Users\SANGWOO\Desktop\VSCODE\엑셀 샘플\통합 문서.xlsx")

# step7. 켜져있는 엑셀 및 어플리케이션 모두 종료
excel.Quit()
