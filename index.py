#C114:しりとりの判定 12/27
n = int(input())
word =  [input() for i in range(n)]
s= 0
for i in range(n-1):
    if word[i][-1] != word[i+1][0]:
        print(word[i][-1] + " " +word[i+1][0])
        break
    else:
       s += 1
if s == n-1:
    print("Yes")

