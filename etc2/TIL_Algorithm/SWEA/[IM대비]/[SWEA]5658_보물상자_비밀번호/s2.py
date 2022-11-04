import sys
sys.stdin = open('input.txt', 'r')


t = int(input())

for tc in range(1, t + 1) :
    n, k = map(int, input().split())
    data = input()
    arr = []
    for j in range(n // 4) :
        for i in range(0, n, n // 4) :
            arr.append(data[i:i+(n//4)])

        data = data[-1] + data[:-1]
    arr = list(set(arr))
    arr.sort(reverse=True)

    result = arr[(k-1) % len(arr)]

    print('#%d %d' % (tc, int(result, 16)))