#C013:嫌いな数字
n = int(input())
m = int(input())
r = [int(input()) for i in range(m)]

a=0
for i in range(m):
    if (str(n) in str(r[i])) == False:
        print(r[i])
        a += 1
if a == 0:
    print("none")
        
