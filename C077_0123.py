import math

k, n = map(int, input().split())

for i in range(k):
    day, ok = map(int, input().split())
    score = 100 / n * ok
    if 0 < day < 10:
        score = int(score * 0.8)
    elif day >= 10:
        score = 0
    
    if 80 <= score:
        print("A")
    elif 70 <= score:
        print("B")
    elif 60 <= score:
        print("C")
    else:
        print("D")