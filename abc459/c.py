N, Q = map(int, input().split())

# masu = [0] * N
masu = []
for i in range(0,N):
    masu.append(0)

while (Q >= 1):
    qa, qb = map(int, input().split())
    if qa == 1:
        masu[qb-1] += 1
        if not 0 in masu:
            masu = [j-1 for j in masu]
    else:
        num = 0
        masu_y = sorted(masu)
        i = -1
        while True:
            if masu_y[i] >= qb:
                num += 1
            else:
                break
            i -= 1
        print(num)
    Q -= 1
