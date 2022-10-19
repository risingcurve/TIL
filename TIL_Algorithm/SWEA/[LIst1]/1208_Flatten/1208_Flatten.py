import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):
        highest = max(arr)
        lowest = min(arr)
        max_idx = arr.index(highest)
        min_idx = arr.index(lowest)
        arr[max_idx] -= 1
        arr[min_idx] += 1
        result = max(arr) - min(arr)
        if result == 0 or result == 1:
            break
        else:
            continue
    print('#{} {}'.format(tc, result))

