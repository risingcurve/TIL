# 4873_반복문자_지우기 풀이
# 2022-08-18

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

# len함수 정의
def my_len(str_A):
    an = 0
    for l in str_A:
        an += 1
    return an

# 문장을 돌며 이전에 담긴 문자와 담으려고 하는 문자가 같다면 제거한다.
for tc in range(1, T + 1):
    s = str(input())
    stack = []
    for i in s:
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    print('#{}'.format(tc), my_len(stack))
