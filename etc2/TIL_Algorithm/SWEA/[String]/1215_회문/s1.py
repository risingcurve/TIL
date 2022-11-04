# 1215_회문1

import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    board = [list(input()) for _ in range(8)]

    cnt = 0
		
		# 가로
    for i in range(8):
        for j in range(8 - N + 1):
            if board[i][j:j+N] == board[i][j:j+N][::-1]:
                cnt += 1

		# 세로
    for j in range(8):
        for i in range(8 - N + 1):
						# 세로 문장을 확인하기 위해 빈 문자열 변수 생성
            char = ''
						# i번째 행부터 회문의 길이만큼 문자열을 변수에 저장
            for k in range(i, i + N):
                char += board[k][j]
            if char == char[::-1]:
                cnt += 1

    print('#{} {}'.format(tc, cnt))