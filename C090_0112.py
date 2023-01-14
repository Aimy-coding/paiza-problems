n = list(map(int,input().replace("-", "")))
answer =0
for i in range(len(n)):
    if n[i] == 0:
        answer += 12*2
    else:
        answer += (n[i]+2)*2
print(answer)


###別解###
S = input() #電話番号
distance = [12, 3, 4, 5, 6, 7, 8, 9, 10, 11] #0~9の番号までの距離
ans = 0

for i in S:
    if(i >= "0" and i<= "9"):
        ans += distance[int(i)] * 2

print(ans)        