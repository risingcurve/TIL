adj_list = [[1, 2],
            [0, 3, 4],
            [0, 4],
            [1, 5],
            [1, 2, 5],
            [3, 4, 6],
            [5]]

def dfs(v, N):
    visited = [0] * N   # visited 생성
    stack = [0] * N     # stack 생성
    top = -1

    print(v)
    visited[v] = 1
    while True:
        for w in adj_list[v]:
            if visited[w] == 0:
                top += 1
                stack[top] = v
                v = w
                print(v)
                visited[w] = 1
                break
        else:
            if top != -1:
                v = stack[top]
                top -= 1
            else:
                break

dfs(1, 7)
