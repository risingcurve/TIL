import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    charge = list(map(int, input().split()))
    plan = [0] + list(map(int, input().split()))
    
    dp = [0] * 13
    for i in range(1, 13):
        dp[i] = dp[i-1] + min(charge[0] * plan[i], charge[1])
        if i > 2:
            dp[i] = min(dp[i], dp[i-3] + charge[2])
    result = min(dp[12], charge[3])
    print('#{} {}'.format(tc, result))
