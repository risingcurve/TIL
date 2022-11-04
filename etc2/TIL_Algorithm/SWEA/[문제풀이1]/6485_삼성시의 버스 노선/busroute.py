# 6485_삼성시의 버스노선 풀이
# 2022-08-19

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 1번부터 5000번까지 정류장(0번 인덱스는 의미 없음)
    stop = [0] * 5001

    # N만큼 반복
    for i in range(1, N + 1):
        Ai, Bi = map(int, input().split())
        for j in range(Ai, Bi + 1):
            stop[j] += 1

    # P개의 버스 정류장
    P = int(input())

    # P개의 버스 정류장을 저장하는 리스트
    p_list = []

    # P만큼 반복
    for i in range(P):
        stop_num = int(input())
        p_list.append(stop_num)

    print('#{}'.format(tc), end=' ')
    for i in p_list:
        print(stop[i], end=' ')
    print()
