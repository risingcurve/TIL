# 5174_subtree_풀이
# 2022-09-15

import sys
sys.stdin = open('input.txt', 'r')

def inorder_traverse(node):
    global cnt
    if node == 0:
        return
    cnt += 1

    inorder_traverse(left[node])
    inorder_traverse(right[node])

T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    left = [0] * (E + 2)
    right = [0] * (E + 2)

    for i in range(0, len(arr), 2):
        par, cdr = arr[i], arr[i + 1]
        if left[par]:
            right[par] = cdr
        else:
            left[par] = cdr

    cnt = 0
    inorder_traverse(N)
    print('#{} {}'.format(tc, cnt))