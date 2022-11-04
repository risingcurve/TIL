import sys
sys.stdin = open('input.txt', 'r')

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
 
    i, j, dr = 0, 0, 0
 
    for cnt in range(1, N*N+1):
        arr[i][j]=cnt
        ni, nj = i+di[dr], j+dj[dr]

        if 0<=ni<N and 0<=nj<N and arr[ni][nj]==0:
            i, j = ni, nj
        else:
            dr = (dr+1)%4
            i,j = i+di[dr], j+dj[dr]
 
    print('#{}'.format(tc))
    for lst in arr:
        print(*lst)