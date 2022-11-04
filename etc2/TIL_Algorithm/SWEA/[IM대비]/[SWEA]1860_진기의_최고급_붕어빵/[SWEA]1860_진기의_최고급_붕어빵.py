# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()

    ans = 'Possible'
    cnt = 0
    for i in arr:
        cnt += 1
        if cnt > (i//M)*K:
            ans = 'Impossible'
            break

    print('#{} {}'.format(tc, ans))