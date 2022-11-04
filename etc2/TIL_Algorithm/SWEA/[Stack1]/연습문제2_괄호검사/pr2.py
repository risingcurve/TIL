# 연습문제2_괄호검사_풀이
# 2022-08-18

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    parenthesis = input()
    stack = []

    result = 1
    for i in parenthesis:
        if i =='(':
            stack.append(i)
        elif i != '(' and stack:
            stack.pop()
        else:
            result = 0

    if stack:
        result = 0
    
    print('#{} {}'.format(tc, result))