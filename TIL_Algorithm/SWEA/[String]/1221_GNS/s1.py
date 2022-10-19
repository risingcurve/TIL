# 1221_GNS 풀이
# 2022-08-12

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

strnum_list = ["ZRO","ONE","TWO","THR","FOR","FIV","SIX","SVN","EGT","NIN",]

for tc in range(1, T + 1):

    N, M = input().split()
    numbers_list = list(map(str,input().split()))

    result = [] # 결과를 저장할 리스트

    # 리스트 내 문자열이 의미하는 값과 인덱스의 값을 맞춰, 
    # 인덱스로 값에 접근하여 리스트 result에 추가
    for i in range(T):
        for j in numbers_list:
            if strnum_list[i] == j:
                result.append(j)

    print(N)
    print(*result)