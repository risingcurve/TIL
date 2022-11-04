import sys
import heapq

sys.stdin = open('input.txt')

T = int(input())

INF = 1234567890

for tc in range(1, T + 1):
    N = int(input())  
    matrix = []  # 테두리를 설정 할 것이기 때문에 list Comprehension을 쓰기에 조금 어렵....ㅎ
    matrix.append([INF] * (N + 2))  # 가장 윗부분 테두리를 추가합니다.
    for _ in range(N):
        matrix.append([INF] + list(map(int, input())) + [INF])  # 가장 왼쪽과 오른쪽에 테두리를 추가
    matrix.append([INF] * (N + 2))  # 가장 아랫줄 테두리를 추가

    dist = [
        [INF] * (N + 2) for _ in range(N + 2)
    ]  # (1,1)에서부터의 거리행렬. N*N행렬에다가 테두리에 INF를 추가했다고 생각해봐용 (총 N+2 * N+2)

    que = []

    heapq.heappush(que, [0, 1, 1])  # heap에 [거리, x좌표, y좌표]를 차례로 넣어유
    dist[1][1] = 0  # 거리는 0으로 초기화합니다

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]  # 이차원 배열에서 이동 방향을 설정

    while que:  # que가 비어있을 때까지 반복합니다.
        di, x, y = heapq.heappop(que)  # que에서 [거리, x좌표, y좌표]를 뽑고
        if x == N and y == N:
            break
        if di > dist[x][y]:
            continue
        for dx, dy in zip(dx, dy):  # 총 4개의 방향에 대해서
            nx, ny = x + dx, y + dy
            if dist[nx][ny] > di + matrix[nx][ny]:  # 다음 위치의 거리가 현재 위치에서 갈 때 더 거리가 작으면
                dist[nx][ny] = di + matrix[nx][ny]  # 거리를 최신화
                heapq.heappush(que, [dist[nx][ny], nx, ny])  # que에 넣어줘요

    print('#{} {}' .format(tc, dist[N][N])) # (N,N)까지의 거리를 출력하면 끝