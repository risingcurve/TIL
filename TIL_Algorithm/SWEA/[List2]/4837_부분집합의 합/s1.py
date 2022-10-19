# 220811
# 4837 부분집합의 합

# 정답 코드 

import sys
sys.stdin = open('input.txt', 'r')

A = list(range(1, 13))

T = int(input())

      
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    cnt = 0

    # 비트 연산자를 통해 부분집합의 합 구하기
    for i in range(1<<12):
        len_subset = 0 # 부분집합의 원소의 수
        sum_subset = 0 # 부분집합의 합
        for j in range(12):
            if i & (1<<j):
                sum_subset += A[j]
                len_subset += 1

                # 부분집합의 원소의 수가 N보다 많아지면 if문 탈출
                if len_subset > N:
                    break
        if len_subset == N and sum_subset == K:
            cnt += 1

    print('#{} {}'.format(tc, cnt))

