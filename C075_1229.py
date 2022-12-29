
import math
n, m = map(int, input().split())
f = [int(input()) for i in range(m)]

p = 0
for i in range(m):
    if p >= f[i]:
        p -=f[i]
        print(n, p)
    else:
        n= n-f[i]
        p += math.floor(f[i]*0.1)
        print(n, p)