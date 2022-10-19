import sys
sys.stdin = open('input.txt', 'r')

def swap(prize, i, j):
    # itoa
    prize_arr = [0] * prize_len
    for k in range(prize_len - 1, -1, -1):
        prize_arr[k] = prize % 10
        prize //= 10
    # swap
    prize_arr[i], prize_arr[j] = prize_arr[j], prize_arr[i]
    # atoi
    prize = 0
    for k in range(prize_len):
        prize = prize * 10 + prize_arr[k]
    
    return prize


def find_max(n, k, prize):
    global ans
    ###############
    # 가지 치기
    for i in range(720):
        if memo[k][i] == 0:
            memo[k][i] = prize
            break
        elif memo[k][i] == prize:
            return 
    ###############

    if n == k: # 최대값 유지
        if prize > ans:
            ans = prize
    else: # 숫자판 길이에서 2를 선택
        for i in range(prize_len - 1):
            for j in range(i + 1, prize_len):
                find_max(n, k + 1, swap(prize, i, j))

T = int(input())
for tc in range(1, T + 1):
    # 숫자판, 횟수
    prize, N = map(int, input().split())
    memo = [[0] * 720 for _ in range(N + 1)]
    # 숫자판의 길이
    prize_len = 0
    t = prize
    while t:
        t //= 10
        prize_len += 1

    ans = 0
    find_max(N, 0, prize)
    print('#{} {}'.format(tc, ans))
