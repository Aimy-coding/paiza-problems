n, r = map(int, input().split())
s = [input() for i in range(n)]
answer=[]

for i in range(n):
    a, b, c = map(int, s[i].split())
    if a >= r*2 and b>= r*2 and c >= r*2:
        answer.append(i)
for i in range(len(answer)):
    print(answer[i] +1)