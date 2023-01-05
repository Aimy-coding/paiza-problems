#c117
x, y, z = map(int, input().split())

n = int(input())
r = [input() for i in range(n)]
s=0
time = {}
for i in range(0, 23):
    if 9 <=i and i <=16:
        time[i] =x
    elif 17<= i and i <=21:
        time[i] = y
    else:
        time[i] =z
        

for i in range(n):
    a, b = map(int, r[i].split())
    for i2 in range(a, b):
        s += time[i2]
        
print(s)