# 9367_점점 커지는 당근의 개수
# 2022-08-19

import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    C = list(map(int, input().split()))

    cnt = 1
    cnt_list = []

    # 당근이 커질 때마다 커지는 당근 개수 1씩 추가
    for i in range(1, N):
        if C[i] > C[i-1]:
            cnt += 1
            cnt_list.append(cnt)
        # 안 커질 때 초기화
        else:
            cnt = 1

    # 최대값 뽑아내기
    max_cnt = 1
    for i in cnt_list:
        if max_cnt <= i:
            max_cnt = i

    print('#{} {}'.format(tc, max_cnt))