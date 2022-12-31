import re
n = int(input())
s = [input() for i in range(n)]
answer={}
for i in range(n):
    answer[int(re.sub(r"\D", "", s[i]))] = s[i]

answer = sorted(answer.items())
answer = dict((x,y) for x,y in answer)
answer = list(answer.values())


for i in range(n):
    print(answer[i])