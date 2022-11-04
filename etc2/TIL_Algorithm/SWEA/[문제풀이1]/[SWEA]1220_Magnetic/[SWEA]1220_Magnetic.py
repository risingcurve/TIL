import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    table = [list(input().split()) for _ in range(N)]
    cnt = 0

    for i in range(N):
        tmp = ''
        for j in range(N):
            tmp += table[j][i]
        cnt += tmp.replace("0","").count("12")
    print("#{} {}".format(tc, cnt))

# for tc in range(1, 11):
#     N = int(input())
#     table = [list(map(int, input().split())) for _ in range(100)]
#     cnt = 0
#     for i in range(N):
#         basket = []

# # 교착 상태가 아닌 자성체 떨어뜨리기
# for i in range(100):
#     for j in range(100):
#         for k in range(1, 100):
#             if i+k <= 99 and i-k >= 0:
#                 if table[i][j] == 1 and table[i+k][j] != 2:
#                     table[i][j] = 0

#                 if table[i][j] == 2 and table[i-k][j] != 1:
#                     table[i][j] = 0

# # 교착 상태의 자성체 새로운 리스트에 담기
# for i in range(100):
#     for j in range(100):
#         if table[i][j] == 1 or table[i][j] ==2:
#             basket.append(table[i][j])


# # print('#{} {}'.format(tc, len(basket)))