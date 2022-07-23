year = int(input())
if ( (year % 4 ==0 #연도가 4로 나누어 떨어진다.
    and year % 100 != 0) #100으로 나누어 떨어지는 연도 제외한다.
    or year % 400 == 0): #400으로 나누어 떨어지는 연도는 윤년이다.

    print(year, "년은 윤년입니다.")
else :
    print(year, "년은 윤년이 아닙니다.")