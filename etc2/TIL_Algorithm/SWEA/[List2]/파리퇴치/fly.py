import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    fly_board = [list(map(int, input().split())) for _ in range(N)]

    fly_plus = [[0] * N for _ in range(N)]
    fly_x = [[0] * N for _ in range(N)]
    result_list = []
    # result_board = [[0] * N for _ in range(N)]
    result = 0

    for i in range(N):
        for j in range(N):

            for k in range(M):
                if i + k <= N - 1:
                    fly_plus[i][j] += fly_board[i + k][j]
                if i - k >= 0:
                    fly_plus[i][j] += fly_board[i - k][j]
                if j + k <= N - 1:
                    fly_plus[i][j] += fly_board[i][j + k]
                if j - k >= 0:
                    fly_plus[i][j] += fly_board[i][j - k]
            fly_plus[i][j] -= (fly_board[i][j] * 3)
            result_list.append(fly_plus)

            for k in range(M):
                if i + k <= N - 1 and j + k <= N - 1:
                    fly_x[i][j] += fly_board[i + k][j + k]
                if i - k >= 0 and j + k <= N - 1:
                    fly_x[i][j] += fly_board[i - k][j + k]
                if i + k <= N - 1 and j - k >= 0:
                    fly_x[i][j] += fly_board[i + k][j - k]
                if i - k >= 0 and j - k >= 0:
                    fly_x[i][j] += fly_board[i - k][j - k]
            fly_x[i][j] -= (fly_board[i][j] * 3)
            result_list.append(fly_x)

    for i in result_list:
        if i 

    # for k in range(N):
    #     for l in range(N):
    #         if fly_plus[k][l] > fly_x[k][l]:
    #             result_board[k][l] += fly_plus[k][l]
    #         else:
    #             result_board[k][l] += fly_x[k][l]

    result = max(map(max, result_board))

    print('#{} {}'.format(tc, result))
