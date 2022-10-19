import sys
sys.stdin = open('input.txt', 'r')

T = int(input())



for tc in range(1, T + 1):
    cnt_plus = 0
    cnt = 0
    arr = list(map(str, input()))

    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr) - 2):
            if arr[i] == 'O': 
                cnt += 1
                if arr[i + j] == 'O':
    print(arr)
