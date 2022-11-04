def solve():
    for si in range(N):
        for sj in range(N):     # 가능한 모든 시작위치
            for di,dj in ((0,1),(1,1),(1,0),(-1,1)):
                for mul in range(5):
                    ni,nj = si+di*mul, sj+dj*mul
                    # 범위밖이거나 범위내이지만 오목알이 아니면 break
                    if ni<0 or ni>=N or nj<0 or nj>=N or arr[ni][nj]!='o':
                        break
 
                    # 범위내이고 오목알이면 통과, 아니면 break
                    # if 0<=ni<N and 0<=nj<N and arr[ni][nj]=='o':
                    #     pass
                    # else:
                    #     break
                else:
                    return 'YES'
    return 'NO'
 
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]
 
    ans = solve()
    print(f'#{test_case} {ans}')