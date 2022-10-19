import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
arr = list(map(int, input().split()))

basket = []

for i in range(N - K + 1):
    a = sum(arr[i:i+K])
    basket.append(a)
result = max(basket)

print(result)