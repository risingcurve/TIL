# 미리 일꾼이 모을 수 있는 벌꿀의 양을 모아놓고, 그것들 중 2개를 고름
def honey(x,y):
    tmp = lst[x][y:y+m]
    res = 0
    for i in range(2**m):
        tmp_res = 0
        tmp_squre = 0
        use = queue[i]
        for j in range(m):
            if use[j] == "1":
                tmp_res += tmp[j]
                tmp_squre += tmp[j]**2
        if tmp_res <= c and tmp_squre >= res:
            res = tmp_squre
    return res



T = int(input())
for tc in range(1, T+1):
    n, m, c = map(int,input().split())
    lst = [list(map(int,input().split())) for _ in range(n)]

    queue = [list(bin(i)[2:].zfill(m)) for i in range(2**m)]

    honey_lst = [[0]*(n-m+1) for _ in range(n)]

    for i in range(n):
        for j in range(n-m+1):
            honey_lst[i][j] = honey(i,j)
            
    res = sum(sorted([max(x) for x in honey_lst], reverse=True)[:2])
    for i in range(n):
        for j in range(n-2*m+1):
            tmp = honey_lst[i][j]
            for k in range(j+m, n-m+1):
                if tmp + honey_lst[i][k] > res:
                    res = tmp + honey_lst[i][k]


    print("#{} {}".format(tc, res))