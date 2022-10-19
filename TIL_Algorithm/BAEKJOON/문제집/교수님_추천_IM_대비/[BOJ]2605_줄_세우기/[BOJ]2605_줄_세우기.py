def line(n):
    basket.insert(n, cnt)

N = int(input())
arr = list(map(int, input().split()))

cnt = 0
basket = []
for i in range(N):
    cnt += 1
    line(arr[i])

basket.reverse()

for i in basket:
    print(i, end=' ')