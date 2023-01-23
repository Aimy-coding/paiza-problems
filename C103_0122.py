n, m =map(int, input().split())
moving = [list(map(str, input().split())) for i in range(m)]


ugoki =[]
for i in range(m):
    ugoki.append(int(moving[i][0]))

  


for i in range(1, n+1):
    ans = []
    for j in range(len(moving)):
        if i % int(moving[j][0]) == 0:
            ans.append(moving[j][1])
    if ans == []:
        print(i)
      
    else:
        print(" ".join(ans))