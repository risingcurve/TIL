import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    building_list = list(map(int, input().split()))

    view = 0

    for i in range(2, N - 2):
        a = building_list[i] - building_list[i - 2]
        b = building_list[i] - building_list[i - 1]
        c = building_list[i] - building_list[i + 1]
        d = building_list[i] - building_list[i + 2]
        if a > 0 and b > 0 and c > 0 and d > 0:
            view += min(a, b, c, d)

    print('#{} {}'.format(tc, view))
