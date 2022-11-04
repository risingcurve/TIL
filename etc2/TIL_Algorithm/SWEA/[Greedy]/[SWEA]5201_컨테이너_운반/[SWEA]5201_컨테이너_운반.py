import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    ct = list(map(int, input().split()))
    tr = list(map(int, input().split()))
    
    ct.sort(reverse=True)
    tr.sort(reverse=True)
    
    result = [0 for _ in range(M)]

    for i in range(N):
        for j in range(M):
            if ct[i] <= tr[j]:
                if result[j] == 0:
                    result[j] = ct[i]
                    break

    print('#{} {}'.format(tc, sum(result)))