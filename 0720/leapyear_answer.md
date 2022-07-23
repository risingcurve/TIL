year = int(input())

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print('{}은 윤년입니다.' .format(year)) #f'string을 사용할 수 있지만 swea에서 못 함.
else:
    print('{}은 윤년이 아닙니다.' .format(year))


----
year = int(input())

def leap_year(year):
if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    return True
    print('{}은 윤년입니다.' .format(year)) #f'string을 사용할 수 있지만 swea에서 못 함.
else:
    return False
    print('{}은 윤년이 아닙니다.' .format(year))

-------------

def leap_year(year):
    flag = True
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        flag == True
    else:
        flag = False

answer = lear_year(year)

if answer == True:
    print('{}은 윤년입니다.' .format(year)) 
else:
    print('{}은 윤년이 아닙니다.' .format(year))

----------------------

def leap_year(year):
    import calendar
    if calendar.isleap(year):
        #True
        