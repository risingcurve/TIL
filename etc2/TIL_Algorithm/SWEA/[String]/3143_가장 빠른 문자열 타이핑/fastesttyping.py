# 3143_가장 빠른 문자열 타이핑 풀이
# 2022-08-16

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

# 길이 구하는 함수 정의
def my_len(str_A):
    res = 0
    for i in str_A:
        res += 1
    return res

# 'str1 문자열의 길이'에서 'str2 문자열의 길이-1 * 반복된 수' 만큼 뺀다.
for t in range(1, T+1):
    str1, str2 = map(str, input().split())
    result = my_len(str1) - ((my_len(str2)-1)*str1.count(str2))

    print('#{} {}'.format(t, result))