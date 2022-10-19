# 연습문제1_스택구현
# 2022-08-17

stack = [0]*3 # 사이즈 먼저 설정
top = -1 # top 초기값을 -1로 설정

# top을 하나 증가시키고 top 위치에 데이터 저장
top += 1
stack[top] = 1

top += 1
stack[top] = 2

top += 1
stack[top] = 3

# top을 하나 내리고 내리기 전 데이터 반환
top -= 1
data = stack[top+1]
print(data)

top -= 1
data = stack[top+1]
print(data)

top -= 1
data = stack[top+1]
print(data)

# .append()를 이용하여 데이터 추가
stack2 = []
stack2.append(1)
stack2.append(2)
stack2.append(3)
# .pop()을 이용하여 데이터 추출
print(stack2.pop())
print(stack2.pop())
print(stack2.pop())