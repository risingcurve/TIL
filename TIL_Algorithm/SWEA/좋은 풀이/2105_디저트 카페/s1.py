import sys

sys.stdin = open('input.txt')


def DFS(r, c, direction, cnt):  # direction: 방향, cnt:진행한 칸 수
    global save_row, save_col, max_value

    if 0 <= r < N and 0 <= c < N:  # 범위 체크
        if direction == 3 and r == save_row and c == save_col:  # 출발점에 도착한 경우
            if max_value < cnt:  # 최댓값 갱신
                max_value = cnt
        elif G[r][c] in dessert:  # 이미 먹은 디저트가 있는 경우 종료
            return
        elif direction == 2 and max_value > 2 * cnt:
            return
        else:
            dessert.append(G[r][c])
            if direction == 0 or direction == 1:  # 오른쪽 아래로 또는 왼쪽 아래로 가는 경우
                # k 방향으로 계속 가거나
                DFS(r + dr[direction], c + dc[direction], direction, cnt + 1)
                # k+1 방향으로 전환
                DFS(
                    r + dr[direction + 1], c + dc[direction + 1], direction + 1, cnt + 1
                )
            elif direction == 2:
                if r + c != save_row + save_col:  # 출발점을 향할 때가 아니면 직진
                    DFS(r + dr[2], c + dc[2], direction, cnt + 1)
                else:
                    DFS(r + dr[3], c + dc[3], direction + 1, cnt + 1)
            else:  # k==3 직진
                DFS(r + dr[3], c + dc[3], direction, cnt + 1)

            dessert.remove(G[r][c])


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    G = [list(map(int, input().split())) for _ in range(N)]

    # 대각 이동
    dr = [1, 1, -1, -1]
    dc = [1, -1, -1, 1]
    max_value = -1
    dessert = []

    for row in range(N):
        for col in range(1, N - 1):
            save_row = row
            save_col = col
            dessert.append(G[row][col])
            DFS(row + 1, col + 1, 0, 1)
            dessert.remove(G[row][col])
    
    print('#{} {}' .format(tc, max_value))