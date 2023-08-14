import xlwings

def main():
    # xlwings 통해 Workbook 호출
    wb = xlwings.Book.caller()

    # Sheet 설정
    sheet = wb.sheets[0]

    # 텍스트 입력
    sheet["A1"].value = "xlwings 테스트 코드 작성"
    sheet["A2"].value = "파이썬 업무 자동화"

if __name__ == "__main__":
    path = r"C:\Users\wonjong.han\Desktop\RPA\xlwings"

    # 매크로 파일 설정
    xlwings.Book(path+"/"+"p1.xlsm").set_mock_caller()

    # main 함수 호출
    main()


