n, x, y = map(int, input().split())

for i in range(1, n+1):
    if i % x == 0 and i % y == 0:
        print("AB")
    elif i % y == 0:
        print("B")
    elif i % x == 0:
        print("A")
    else:
        print("N")