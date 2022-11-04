import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

basket = []

for i in range(N - K + 1):
    basket.append(sum(arr[i:i+K]))

print(max(basket))



















# basket = []
#
# for i in range(N - K + 1):
#     a = 0
#     for j in range(K):
#         a += arr[i + j]
#     basket.append(a)
#
# result = max(basket)
#
# print(result)
