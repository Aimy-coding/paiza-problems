n = int(input())
s = list(map(int, input().split()))
a, q = map(int, input().split())
x = [input() for i in range(q)]


for i in x:
   price, number = map(int, i.split())
   if int(s[price-1] * number) <=a:
       a -= int(s[price-1] * number)
    
print(a)