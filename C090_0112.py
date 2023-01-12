n = list(map(int,input().replace("-", "")))
answer =0
for i in range(len(n)):
    if n[i] == 0:
        answer += 12*2
    else:
        answer += (n[i]+2)*2
print(answer)
        