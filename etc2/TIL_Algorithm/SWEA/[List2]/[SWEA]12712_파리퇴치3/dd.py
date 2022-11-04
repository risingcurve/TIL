def rotate_90(arr):
    N = len(arr)
    ret = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ret[j][N-1-i] = arr[i][j]
    return ret

area = [
    [1, 2, 3, 4], 
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    ]

print(rotate_90(area))