import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    board = [list(map(str, input().split())) for _ in range(5)]
