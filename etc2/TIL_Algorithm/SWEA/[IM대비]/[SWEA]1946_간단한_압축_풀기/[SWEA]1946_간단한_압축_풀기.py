import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = ''
    for n in range(N):
        al, num = map(str, input().split())
        arr += al * int(num)

    print('#{}'.format(tc))
    for i in range(0, len(arr), 10):
        print(arr[i:i + 10])