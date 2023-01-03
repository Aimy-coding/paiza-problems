#C055:ログのフィルター
n = int(input())
b = str(input())

s = [str(input()) for i in range(n)]
a=0
for i in range(n):
    if (b in str(s[i])) == True:
        print(s[i])
        a += 1
if a == 0:
    print("None")