import sys
sys.stdin = open('input.txt')

"""
N = 1 -> 1
N = 2 -> 0
N = 4 -> 2
N = 8 -> 92 
N = 9 -> 352

문제 풀이 핵심
1. 결국 DFS를 활용해 문제를 풀어간다.
 - 단, 하나도 빠짐없이 탐색하는 것이 아니라 불가능한 선택지를 제거(prunning)하며 문제를 해결
2. 유망한(가능성이 있는) 노드만 검사하고 없다면 부모 노드로 돌아가서 이후에 탐색을 진행
 - 부모 노드로 돌아가는 행위가 Backtracking!
"""

# 유망한 노드 여부를 판별 -> backtracking의 핵심
# 여기서 유망함수는 같은 열/대각선에 놓이는지 여부 체크

def promising(v):
    for i in range(v):
        """
        row[v] == row[i] -> 같은 열에 위치! -> 유망하지 않음
        row[v] == v - i와 같다? -> 같은 대각선 위치! -> 유망하지 않음
        """
        # 유망하지 않음
        if row[v] == row[i] or abs(row[v] - row[i]) == v - i: return False
    # 유망함
    return True

def dfs(v):
    # queen을 배치할 수 있는 가짓수 체크
    
    global cnt
    # 만약 row의 길이와 같다면? queen을 체스판에 모두 놓았다는 의미
    # 즉, 가지치기 되지 않고 마지막 row의 column까지 모두 확인 끝
    if v == len(row):
        # 모든 퀸을 배치 -> count
        cnt += 1
        # print(row[:v+1])
    # 아니라면
    else:
        # 모든 자식 노드 체크
        for i in range(len(row)):
            # row의 v를(column) i로 두고 (i -> 0, 1, 2, 3)
            # 모든 column을 체크해보자
            row[v] = i
            # print(row)
            """
            Prunning -> 가지치기
             - 그냥 방문하는 것이 아닌 유망(가능성) 여부를 판단해서 탐색
             - 현재의 v가 유망한지 여부 판단
            """
            if promising(v):
                # 유망하다면 다음 v 확인
                dfs(v+1)

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 체스판의 크기
    cnt = 0          # Queen을 배치할 수 있는 가짓수 체크
    row = [0] * N    # N 크기만큼의 row -> 여기에 놓은 것을 기준으로 판단할 것
    dfs(0)

    print('#{} {}' .format(tc, cnt))