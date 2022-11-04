for si in range(N):
    for sj in range(N):
        for di, dj in ((0,-1), (0, 1), (-1, 0), (1, 0)):
            for mul in range(M):
                ni, nj = si+di*mul, sj+dj*mul
                if 0 <= ni < N and 0 <= nj < N