d = [0] * 100

d[1] = 1
d[2] = 1
N = 99

for i in range(3, N + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[N])