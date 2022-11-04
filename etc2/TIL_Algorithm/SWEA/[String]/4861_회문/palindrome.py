import sys
sys.stdin = open('sample_input.txt', 'r')

# Test_case = int(input())
#
# for t in range(1, Test_case + 1):
#     N, M = map(int, input().split())
#     result = []
#
#     #배열 입력 받기
#     arr = []
#     for i in range(N):
#         arr.append(input())
#
#     #가로 검색
#     for r in range(N):  #r은 row c는 column
#         for c in range(N - M + 1):
#             if arr[r][c : c + M] == arr[r][c : c + M][ : : -1]: #회문이 맞는지 확인
#                 result.append(arr[r][c : c + M]) #회문이면 결과 리스트에 추가
#
#     #세로 검색
#     for r in range(N - M + 1):
#         for c in range(N):
#             c_list = []  # 새로 열 리스트를 만들어주기
#             for i in range(M):
#                 c_list.append(arr[r+i][c])
#             if c_list == c_list[ : : -1]:  # 세로줄이 회문이면
#                 result.append(''.join(c_list)) #결과리스트에 추가.
#
#     print('#{} {}'.format(t, result[0]))


T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    palindrome_list = []

    arr = []
    for i in range(N):
        arr.append(input())

    for r in range(N):
        for c in range(N - M + 1):
            if arr[r][c : c + M] == arr[r][c : c + M][ : : -1]:
                palindrome_list.append(arr[r][c : c + M])

    for r in range(N - M + 1):
        for c in range(N):
            column_list = []
            for i in range(M):
                column_list.append(arr[r+i][c])
            if column_list == column_list[ : : -1]:
                palindrome_list.append(''.join(column_list))

    print('#{} {}'.format(t, palindrome_list[0]))