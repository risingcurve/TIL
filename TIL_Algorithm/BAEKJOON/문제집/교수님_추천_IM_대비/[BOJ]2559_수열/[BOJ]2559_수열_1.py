import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
arr = list(map(int, input().split()))

basket = []

for i in range(N - K + 1):
    a = 0
    for j in range(K):
        a += arr[i + j]
    basket.append(a)

result = max(basket)

print(result)
