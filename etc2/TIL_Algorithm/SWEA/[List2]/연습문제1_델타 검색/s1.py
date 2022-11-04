# 220810
# 델타검색

# 정답 코드
import sys
sys.stdin = open('input.txt', 'r')

T = int(input()) # 테스트케이스 개수

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

# 절대값 구하는 함수 정의
def absV(a):
    if a >= 0:
        return a
    else:
        return -a

for t in range(1, T + 1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 정답을 담을 변수 초기화
    result = 0

    # 모든 요소에 대해서 델타 탐색 시행
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]

                # 유효한 인덱스일 경우 판별
                if 0 <= ni < N and 0 <= nj < N:
                    
                    # 인접한 요소와의 차의 절대값을 result에 더해준다.
                    A = arr[i][j] - arr[ni][nj]
                    result += absV(A)

    print('#{} {}'.format(t, result))
    