# 4864_문자열 비교 풀이
# 2022-08-16

import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

# 문자열을 그대로 받는다.
for t in range(1, T + 1):
    str1 = input()
    str2 = input()
    result = 0

    # str1이 str2 안에 포함되어 있는지 확인.
    if str1 in str2:
        result = 1
    else:
        result = 0

    print('#{} {}'.format(t, result))


