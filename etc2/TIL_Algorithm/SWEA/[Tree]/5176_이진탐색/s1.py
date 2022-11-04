# 5176_이진탐색_풀이
# 2022-09-15

import sys
sys.stdin = open('input.txt', 'r')

def inorder_traverse(value):
    global cnt
    if value <= N:
        inorder_traverse(2 * value)
        tree[value] = cnt
        cnt += 1
        inorder_traverse(2 * value + 1)

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    tree = [0 for _ in range(N + 1)]

    cnt = 1
    inorder_traverse(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))