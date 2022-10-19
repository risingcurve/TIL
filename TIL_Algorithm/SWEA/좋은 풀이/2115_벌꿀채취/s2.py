import sys

#총 M개의 꿀통 배열에서 총 합이 C를 넘지 않으면서 제곱의 합이 최대가 되는 값
def harvest(honeys, M, C): 
    ans = 0 #답으로 반환할 값을 0으로 초기화

    for mask in range(1<<M): # 비트마스크를 이용해 0부터 (2^M)-1까지의 수들을 확인
        harv = [] #수확하는 꿀 배열을 초기화 하고,
        for idx in range(M):
            #mask에 따라 idx번째가 1이면 harv에 추가
            if mask & 1<<idx:
                harv.append(honeys[idx]) 

        #수확하는 꿀의 총 합이 C를 넘지 않으면,
        if sum(harv) <= C:
            temp = 0
            for val in harv:
                temp += val*val #제곱의 합을 계산하고
            ans = max(ans,temp) #ans와 그 값을 비교해 큰 값으로 갱신
    return ans


sys.stdin = open('input.txt') 

T = int(input()) 
for tc in range(1, T+1): 
    N, M, C = map(int,input().split()) 
    farm = [list(map(int,input().split())) for _ in range(N)] #꿀의 양을 2차원 배열로 입력받음
    harv_DP = [[0]*(N-M+1) for _ in range(N)] # 다이나믹 프로그래밍을 쓰면 조금 더 효율적으로 계산 가능
    
    for y in range(N):
        for x in range(N-M+1):
            harv_DP[y][x] = harvest(farm[y][x:x+M], M, C)
            #harv_DP[y][x]는 (x,y)에서 시작해서 가로로 M개를 가져갈 때 얻을 수 있는 최대 가치를 저장
    
    ans = 0
    
    #농부 1의 좌표를 (x1,y1), 그리고 농부 2는 농부 1보다 뒤에 있다고 가정
    for y1 in range(N): 

        # 농부2가 농부1과 같은 행에 있는 경우를 파악 y2=y1이고 x2값은 x1+M부터 N-M까지 가능
        for x1 in range(N-M+1):

            for x2 in range(x1+M,N-M+1): 
                ans = max(ans, harv_DP[y1][x1]+harv_DP[y1][x2])
                #각각의 농부가 (x1,y1) , (x2,y1) 위치에 있을 때 최대 수확을 DP에 저장한 값을 이용해 계산하고 최대값과 비교해 갱신
            
            # 농부2가 농부1 보다 아래 행에 있는 경우를 파악,  y2는 y1+1부터 N-1까지 가능하고, x2는 0부터 N-M까지 가능
            for y2 in range(y1+1,N): 
                
                for x2 in range(N-M+1):
                    ans = max(ans, harv_DP[y1][x1]+harv_DP[y2][x2])
                    #각각의 농부가 (x1,y1) , (x2,y2) 위치에 있을 때 최대 수확을 DP에 저장한 값을 이용해 계산하고 최대값과 비교해 갱신
    
    
    print('#{} {}' .format(tc, ans))