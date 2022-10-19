# 220811
# 4839 이진탐색

# 정답 코드 

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

# 책 페이지는 정렬된 리스트로 볼 수 있으므로 이진탐색 시행할 함수 정의
def binarySearch(page, target):
    left = 1
    right = page
    count = 0 
    while left <= right:
        mid = (left + right) // 2
        if mid == target:
            return count
        elif mid < target:
            left = mid
            count += 1
        elif mid > target:
            right = mid
            count += 1

# A와 B 중 승자 가려내기
for tc in range(1, T + 1):
    page, A, B = map(int, input().split())
    count_A = binarySearch(page, A)
    count_B = binarySearch(page, B)
    if count_A > count_B:
        result = 'B'
    elif count_A < count_B:
        result = 'A'
    else:
        result = 0
    print("#{} {}".format(tc, result))