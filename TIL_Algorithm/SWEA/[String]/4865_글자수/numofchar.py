# 4865_글자수
# 2022-08-16

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

# 문자열을 리스트로 저장
for t in range(1, T+1):
    str1_list = list(input())
    str2_list = list(input())

    count_list = []
    max_value = 0

    # str1_list의 요소와 str2_list 요소를 하나씩 대조.
    # 한 문자당 일치하는 수 만큼 빈 리스트에 추가.
    for i in str1_list:
        cnt = 0
        for j in str2_list:
            if i == j:
                cnt += 1
        count_list.append(cnt)

    # count_list에서 최댓값을 추출.
    for k in count_list:
        if k >= max_value:
            max_value = k

    print('#{} {}'.format(t, max_value))



