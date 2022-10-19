import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_T = list(map(list, zip(*arr)))
    ans = 0

    for i in arr_T:
        a = 0
        for j in i:
            if j:
                if a == 1 and j == 2:
                    ans += 1
                a = j

    print(f'#{tc} {ans}')



'''
T = 10
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_T = list(map(list,zip(*arr)))
    ans = 0
 
    for lst in arr_T:
        prev = 0
        for n in lst:
            if n:       # 0이 아닌경우 (1, 2)
                if prev==1 and n==2:    # 1이 N극
                    ans += 1
                prev = n
 
    print(f'#{test_case} {ans}')
    '''