import  xlwings  as  xw

#엑셀 매크로파일 열기(path는 매크로 파일이 있는 경로)
wb = xw.Book("py1.xlsm")

#엑셀 VBA의 매크로 함수 'test'를 파이썬 함수로 지정
macro_test = wb.macro('test')

#VBA 함수 실행
macro_test()

#함수를 실행한 엑셀파일 따로 저장하기
wb.save("py1_result.xlsm")

#WorkBook 객체 닫기
wb.close