import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(input())

    stack = []
    for i in range(N):
        stack.append(arr[i])

    # N // 4자리씩 빈 문자열에 추가하고, 이를 다시 빈 리스트에 하나씩 넣기
    nums = []
    for i in range(N):
        stack.insert(0, stack[-1])
        stack.pop()
        a = ''
        for j in range(N // 4):
            a += stack[j]
        if a not in nums:
            nums.append(a)

    nums = sorted(nums, reverse=True)
    result = int(nums[K - 1], 16)

    print('#{} {}'.format(tc, result))



