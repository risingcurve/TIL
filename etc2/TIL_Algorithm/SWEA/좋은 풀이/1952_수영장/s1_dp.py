# dp
import sys

sys.stdin = open('input.txt')

T = int(input())

# dp로 구현
for tc in range(1, T + 1):
    # 각 티켓의 요금
    tickets = list(map(int, input().split()))
    # 월별 수영장 이용 계획
    plans = list(map(int, input().split()))

    dp = [0] * 12
    
    for i in range(12):
        # 월별 1일치, 1개월치 사는 것중 더 싼것 기록
        dp[i] = min(dp[i - 1] + plans[i] * tickets[0], dp[i - 1] + tickets[1])

        # 3달 이후부터 3달치도 포함해서 재계산
        if i >= 2:
            # 현재 계산 : 1일치, 1개월치 중 싼것
            # 현재 계산, 3달치 중 싼것
            dp[i] = min(dp[i - 3] + tickets[2], dp[i])

    # 계산 끝난 후, 1년치와 비교
    dp[-1] = min(dp[-1], tickets[3])
    answer = dp[-1]

    print("#{} {}" . format(tc, answer))