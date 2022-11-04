memo = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1

    if memo[x] != 0:
        return memo[x]

    memo[x] = fibo(x-1) + fibo(x-2)
    return memo[x]

print(fibo(int(input())))


'''
def fibo(x):
    global memo
    if n >= 2 and len(memo) <= n :
        memo.append(fibo1(n - 1) + fibo1(n - 2))
    return memo[n]

memo = [0, 1]
'''