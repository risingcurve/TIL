import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    basket = []
    for i in range(N):
        for j in range(N):
            if i >= 0 and j >= 0 and i <= N - 1 and j <= N - 1:
                board[i][j]
