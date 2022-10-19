import sys
sys.stdin = open('input.txt', 'r')

def bracket_check(input_value):
    # 괄호의 짝 딕셔너리
    matching_dict = {')': '('}
    stack = []
    for i in input_value:
        # 열린 괄호를 찾으면 스택에 push
        if i in ('('):
            stack.append(i)
        # 닫힌 괄호를 찾으면
        elif i in (')'):
            # 스택이 비어있거나 괄호의 짝이 맞지 않으면
            if not stack or stack [len(stack) - 1] != matching_dict[i]:
                return 0
            stack.pop() # 짝이 맞으면 pop
    # 검사 후에도 스택에 괄호가 남아 있으면
    if stack:
        return 0
    else:
        return 1


T = int(input())
for tc in range(1, T+1):

    print('#{} {}'.format(tc + 1, bracket_check(input())))