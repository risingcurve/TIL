import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

for tc in range(1, T+1):
    # V : 도착 노드 , E : 간선 갯수
    V, E = map(int, input().split())

    # 인접 리스트로 만들어서 작성.
    graph = [None] * E

    for _ in range(E):
        start, end, dist = map(int, input().split())
        if graph[start]:
            graph[start].append((end, dist))
        else:
            graph[start] = [(end, dist)]

    # 각 노드 별 최소 가중치 합을 저장
    D = [100000000007] * E
    P = [None] * E
    # 방문 확인
    visited = [False] * E

    # 시작점 설정
    D[0] = 0
    visited[0] = True
    for idx in range(E):
        # 인접 경로가 없는 경우
        if graph[idx] == None:
            continue

        # 인접 경로 확인
        for end, w in graph[idx]:
            # 도착 노드의 가중치와 나의 최소가중치의 합이 도착 노드의 가중치 보다 작다면 변경
            # if not visited[end] and w + D[idx] < D[end]:
            if w + D[idx] < D[end]:
                # 가장 짧은 거리로 변경
                D[end] = w + D[idx]
                P[end] = idx
                # 갱신 지점.

                if graph[end] == None:
                    continue
                for r_end, r_w in graph[end]:
                    if r_end != end and  r_w + D[end] < D[r_end]:
                        D[r_end] = r_w + D[end]

        # visited[idx] = True
    
    print('#{} {}'.format(tc, D[V]))