import random

num = random.randint(1,100)
i = 0
x = 0

while x != num:
    i += 1
    x = int(input("1~100 숫자 입력: "))
    
    if x < num:
        print("UP")
    elif x > num:
        print("DOWN")
    elif x == num:
        print(f"정답입니다! {i}회 만에 맞췄어요.")