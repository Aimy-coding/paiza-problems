
#c099 折り紙の貼り合わせ 12/28
n, d = map(int, input().split())
a =  [int(input()) for i in range(n-1)]


weight = d
for i in range(n-1):
    weight += (d-a[i])
    
print(d*weight)