arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

arr_t = list(map(list,zip(*reversed(arr))))
arr_T = list(map(list,zip(*arr)))
print(arr_t)
print(arr_T)
