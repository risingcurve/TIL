import sys
sys.stdin = open('input(1).txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]


    basket = []

    for i in range(N):
        for j in range(N):

            cnt = 0
            ant = 0
            if 0 <= i + K <= N and 0 <= j + K <= N:
                for k in range(K):
                    for l in range(K):
                        cnt += arr[i + k][j + l]

                for m in range(1, K - 1):
                    for n in range(1, K - 1):
                        ant += arr[i + m][j + n]

                basket.append(cnt - ant)

    ans = max(basket)

    print('#{} {}'.format(tc, ans))























# for tc in range(1, T + 1):
#     N, K = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     for i in range(N):
#         for j in range(N):
#             cnt = 0
#             a = 0
#             basket = []
#
#             if 0 <= i + K <= N and 0 <= j + K <= N:
#                 for k in range(K):
#                     cnt += arr[i + k][j + k]
#                 for l in range(1, K - 1):
#                     a += arr[i + l][j + l]
#
#                 basket.append(cnt - a)
#
#     ans = max(basket)
#
#     print('#{} {}'.format(tc, ans))

