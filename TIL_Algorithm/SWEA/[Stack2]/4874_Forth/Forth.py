# 4874_Forth_풀이
# 2022-08-23

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    string = list(map(str, input().split()))
    flag = 0
    stack = []

    try:
        for i in string:
            # 숫자면 스택에 푸시
            if i.isdigit():
                stack.append(int(i))
            # 연산자면 숫자 두 개 꺼내서 연산
            elif i == '+':
                stack.append(stack.pop() + stack.pop())
            elif i == '-':
                stack.append(stack.pop() - stack.pop())
            elif i == '*':
                stack.append(stack.pop() * stack.pop())
            elif i == '/':
                stack.append(stack.pop() / stack.pop())
            else:
                answer = stack.pop()
                # .이 나왔는데 스택에 숫자 남아있으면 실패
                if len(stack) != 0:
                    flag = 1
                break

    # 연산자 나왔는데 스택에 숫자 두개가 없을 때.
    except:
        flag = 1
    if flag:
        print('#{} {}'.format(tc, 'error'))
    else:
        print('#{} {}'.format(tc, answer))


