#c117
n, m = map(int, input().split())
a, b, c = map(int, input().split())
r = [int(input()) for i in range(n)]

answer = 0
for i in range(n):
    if c*r[i] - a - m*b < 0:
        answer +=1
print(answer)