import sys
sys.stdin = open('input.txt', 'r')

T = int(input()) # 테스트케이스 개수

for test_case in range(1, T + 1):
    N = int(input()) # N개의 숫자카드
    A = list(map(int, input())) # input 타입을 int로 변환해서 리스트 A에 넣기

    max_card = A[0] # 카드의 최대값의 초기값 설정.

    for i in A: #리스트 내에서 최대값을 가진 카드 찾기.
        if i > max_card:
            max_card = i

    count_list = [0] * (max_card + 1) #카운트한 개수를 넣을 빈 배열 만들기.
    for j in range(0, N): # 순회하면서 각 카드의 숫자별로 개수 세기.
        count_list[A[j]] += 1 # j값 만큼 count_list의 인덱스로 가서 1씩 더하기.
        
        # 초기값 설정
        max_count = 0
        temp_card = 0

        # count_list를 돌면서 값의 최대를 찾고, 동점인 수가 있다면 그 중 카드 숫자가 더 큰 수를 선택.
        for k in range(0, len(count_list)): 
            if count_list[k] >= max_count: 
                max_count = count_list[k] 
                temp_card = k 

    print('#{} {} {}'. format(test_case, temp_card, max_count))


