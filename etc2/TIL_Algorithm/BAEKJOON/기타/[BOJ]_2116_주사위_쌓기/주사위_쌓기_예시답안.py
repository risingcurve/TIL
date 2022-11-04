def bottom_index(i): # 주사위의 아랫면 숫자 인덱스를 찾아주는 함수
    if i == 0 or i == 5: return abs(i - 5)
    else: return (i + 1) % 4 + 1

def dice_function(i, array, total):
    lst = array[:]
    b_index = bottom_index(i)
    bottom = lst[b_index]
    lst[i] = 0
    lst[b_index] = 0
    total += max(lst)
    return bottom, total

N = int(input())
dice_list =[list(map(int, input().split())) for _ in range(N)]
answer = []

for i in range(len(dice_list[0])):
    total = 0
    bottom, total = dice_function(i, dice_list[0], total)

    for dice in dice_list[1:]:
        t_index = dice.index(bottom)
        bottom, total = dice_function(t_index, dice, total)
    answer.append(total)

print(max(answer))