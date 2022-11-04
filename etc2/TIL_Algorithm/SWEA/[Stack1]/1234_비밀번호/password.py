# 1234_비밀번호 풀이
# 2022-08-18

import sys
sys.stdin = open('input.txt', 'r')

T = 10

for tc in range(1, T + 1):
    n, test_case = input().split()
    n = int(n)
    stack = []
    for i in test_case:
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)

    result = ''.join(stack)

    print('#{} {}'.format(tc, result))