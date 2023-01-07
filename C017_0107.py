a, b = map(int, input().split())
n = int(input())
s = [input() for i in range(n)]

for i in range(n):
    A , B = map(int, s[i].split())
    if a > A:
        print("High")
    elif a ==A and b > B:
        print("Low")
    elif a ==A and b < B:
        print("High")
    elif a < A:
        print("Low")
        