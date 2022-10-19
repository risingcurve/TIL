'''
<백준> 2116. 주사위 쌓기

문제
천수는 여러 종류의 주사위를 가지고 쌓기 놀이를 하고 있다. 주사위의 모양은 모두 크기가 같은 정육면체이며 각 면에는 1부터 6까지의 숫자가 하나씩 적혀있다. 그러나 보통 주사위처럼 마주 보는 면에 적혀진 숫자의 합이 반드시 7이 되는 것은 아니다.

주사위 쌓기 놀이는 아래에서부터 1번 주사위, 2번 주사위, 3번 주사위, … 의 순서로 쌓는 것이다. 쌓을 때 다음과 같은 규칙을 지켜야 한다: 서로 붙어 있는 두 개의 주사위에서 아래에 있는 주사위의 윗면에 적혀있는 숫자는 위에 있는 주사위의 아랫면에 적혀있는 숫자와 같아야 한다. 다시 말해서, 1번 주사위 윗면의 숫자는 2번 주사위 아랫면의 숫자와 같고, 2번 주사위 윗면의 숫자는 3번 주사위 아랫면의 숫자와 같아야 한다. 단, 1번 주사위는 마음대로 놓을 수 있다.

이렇게 쌓아 놓으면 긴 사각 기둥이 된다. 이 사각 기둥에는 4개의 긴 옆면이 있다. 이 4개의 옆면 중에서 어느 한 면의 숫자의 합이 최대가 되도록 주사위를 쌓고자 한다. 이렇게 하기 위하여 각 주사위를 위 아래를 고정한 채 옆으로 90도, 180도, 또는 270도 돌릴 수 있다. 한 옆면의 숫자의 합의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫줄에는 주사위의 개수가 입력된다. 그 다음 줄부터는 한 줄에 하나씩 주사위의 종류가 1번 주사위부터 주사위 번호 순서대로 입력된다. 주사위의 종류는 각 면에 적혀진 숫자가 그림1에 있는 주사위의 전개도에서 A, B, C, D, E, F 의 순서로 입력된다. 입력되는 숫자 사이에는 빈 칸이 하나씩 있다. 주사위의 개수는 10,000개 이하이며 종류가 같은 주사위도 있을 수 있다.



그림 1

출력
첫줄에 한 옆면의 숫자의 합이 가장 큰 값을 출력한다.

예제 입력 1 
5
2 3 1 6 5 4
3 1 2 4 6 5
5 6 4 1 3 2
1 3 6 2 4 5
4 1 6 5 2 3

예제 출력 1 
29


# < 풀이 >
A B C D E F에 각각 0, 1, 2, 3, 4, 5 인덱스를 부여한다.
딕셔너리에 각 면을 키, 마주 보는 면을 밸류로 하여 정의한다(ex, 0 : 5, 1 : 3, ... , 5 : 0).
맨 아래 면을 1부터 시작하여 맨 아래 면과 마주보는 면을 옆면에 올 수있는 면 리스트에서 제외하면 4개의 면이 남는데,
이 중 가장 큰 면을 빈 리스트에 저장한다.
맨 아래 주사위 위에 있는 주사위도 마찬가지로 맨 아랫면과 그 면을 마주보는 면도 옆면에 올 수 있는 리스트에서 제거하여 max_dice_list에 저장한다.
마지막 주사위까지 max_dice_list에 해당 주사위가 옆면에 올 수 있는 최대 값을 저장한다.
이러한 과정을 반복하여 최대 값 리스트들 중에서 가장 큰 값을 결과값으로 출력한다.

'''


import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
dice = [list(map(int, input().split())) for _ in range(n)]
rotate = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
sum_list = []

for i in range(6):
    max_dice_list = []
    bottom_dice = [1,2,3,4,5,6]

    bottom_side = dice[0][i]
    upper_side = dice[0][rotate[i]]

    bottom_dice.remove(bottom_side)
    bottom_dice.remove(upper_side)

    max_dice_list.append(max(bottom_dice))

    for j in range(1, n):
        next_dice = [1,2,3,4,5,6]
        bottom_side = upper_side

        upper_side_index = rotate[dice[j].index(upper_side)]
        upper_side = dice[j][upper_side_index]

        next_dice.remove(bottom_side)
        next_dice.remove(upper_side)

        max_dice_list.append(max(next_dice))

    sum_list.append(sum(max_dice_list))

print(max(sum_list))