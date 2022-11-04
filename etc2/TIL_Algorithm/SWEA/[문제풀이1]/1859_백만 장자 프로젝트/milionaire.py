import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split()))
    last_day = prices[-1]
    cnt = 0

    # 뒤에서 부터 탐색
    for i in range(len(prices) - 1, -1, -1):
        if last_day > prices[i]:
            cnt += last_day - prices[i]
        else:
            last_day = prices[i]
    
    print('#{} {}'.format(tc, cnt))







