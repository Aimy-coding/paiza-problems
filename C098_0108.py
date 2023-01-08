n = int(input())
s = [int(input()) for i in range(n)]
m = int(input())
w = [input() for i in range(m)]


for i in range(m):
     a, b, x = map(int, w[i].split())
     s[b-1] += min(s[a-1], x)
     s[a-1] -= min(s[a-1], x)
            
for i in range(n):
    print(s[i])
            
