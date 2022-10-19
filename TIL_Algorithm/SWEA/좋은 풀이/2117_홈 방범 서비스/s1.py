import sys

sys.stdin = open('input.txt')

T = int(input())


def get_cost(k):  # 비용 계산 함수
    return k**2 + (k - 1) ** 2


def count_house(r1, c1, k):  # 마름모 내 집 개수 확인
    cnt = 0
    for r2, c2 in home:
        if abs(r1 - r2) + abs(c1 - c2) <= k - 1:
            cnt += 1
    return cnt


def check_net(k):  # 이익 확인 및 최대 집 개수 확인: k가 클수록 많은 집을 확보가능
    cost = get_cost(k)

    for i in range(N):
        for j in range(N):
            cnt = count_house(i, j, k)
            net = cnt * M - cost
            if net >= 0 and cnt > result[0]:
                result[0] = cnt

    if result[0]:
        return True


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    result = [0, 0, 0]

    # 집위치 저장
    home = []
    for i in range(N):
        line = list(map(int, input().split()))
        for j in range(N):
            if line[j]:
                home.append((i, j))

    for k in range(N + 2, 0, -1):  # 방범 최대 크기기준 순회
        if check_net(k):
            break

    print('#{} {}' .format(tc, result[0]))