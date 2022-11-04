'''
<백준> 2563. 최댓값

문제
9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

예를 들어, 서로 다른 9개의 자연수

3, 29, 38, 12, 57, 74, 40, 85, 61

이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

입력
첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.

출력
첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.

예제 입력 1 
3
29
38
12
57
74
40
85
61

예제 출력 1 
85
8
'''

# 풀이 1
basket = []

for i in range(9):
    basket.append(int(input()))

max_v = max(basket)
max_idx = basket.index(max_v)

print('{} {}'.format(max_v, max_idx + 1))


# 풀이 2
'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())
i = int(input())

basket = [a,b,c,d,e,f,g,h,i]

max_v = max(basket)
print('{} {}'.format(max_v, basket.index(max_v) + 1))
'''