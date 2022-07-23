# 현재 제 실력으로는 너무 어려운 문제인 것 같습니다...

import random

is_playing = True

while is_playing:
    print('================================')
    print('        Up and Down Game        ')
    print('================================')

    answer = random.randint(1, 10000)  # 1이상 10000이하의 난수
    counts = 0  # 몇 번만에 정답을 맞혔는지 담는 변수

    # 여기부터 코드를 작성하세요.
       
    print(input('1이상 10000이하의 숫자를 입력하세요. :'))

        if 1 <= input() <= 10000:
            
        else:
            print('잘못된 범위의 숫자를 입력하세요. :'input())
            print(input('1이상 10000이하의 숫자를 입력하세요. :'))

