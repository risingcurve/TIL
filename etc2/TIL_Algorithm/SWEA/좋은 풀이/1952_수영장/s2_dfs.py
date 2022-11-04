# recur
import sys
sys.stdin = open('input.txt', 'r')
def func(mon, price):
      global res

      if mon>=12:
          if res>price:
              res = price
          return

      if plan[mon] != 0:
          func(mon+1, price + day*plan[mon])  # 하루치
          func(mon+1, price + month)          # 한달치
          func(mon+3, price + months)         # 세달치
      else:
          func(mon+1, price)


T = int(input())
for tc in range(1, T+1):
    day, month, months, year = map(int,input().split())
    plan = list(map(int,input().split()))

    res = year

    func(0, 0)
		
    print("#{} {}" .format(tc, res))