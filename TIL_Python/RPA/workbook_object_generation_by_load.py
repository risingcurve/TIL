import openpyxl as op

path = r"C:\Users\wonjong.han\Desktop\RPA"

wb = op.load_workbook(path + "/RPA.xlsx")

print(wb)

