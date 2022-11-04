import sys
sys.stdin = open('input.txt', 'r')

T = int(input()) # 테스트케이스 개수

for test_case in range(1, T + 1):
    
    N = int(input()) # N개의 양수
    A = list(map(int, input().split())) # input 타입을 int로 변환해서 리스트 A에 넣기

    max_A = A[0] # 최대값을 A의 첫번째 원소로 초기화

    # 버블정렬의 원리를 이용하여 max_A 갱신
    for i in A:
        if i >= max_A:
            max_A = i


    min_A = A[0] # 최소값을 A의 첫번째 원소로 초기화

    # 버블정렬의 원리를 이용하여 min_A 갱신
    for j in A:
        if j <= min_A:
            min_A = j
                    
    print('#{} {}' .format(test_case, max_A-min_A))