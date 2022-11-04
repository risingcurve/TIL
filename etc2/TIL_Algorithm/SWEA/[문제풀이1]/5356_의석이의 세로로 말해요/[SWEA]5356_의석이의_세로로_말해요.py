import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    board = [list(map(str, input())) for _ in range(5)]
    new_board = [[0] * 15 for _ in range(15)]
    for i in range(len(board)):
        for j in range(len(board[i])):
            new_board[i][j] = board[i][j]

    result = ''
    for i in range(15):
        for j in range(15):
            if new_board[j][i] != 0:
                result += new_board[j][i]

    print('#{} {}'.format(tc, result))