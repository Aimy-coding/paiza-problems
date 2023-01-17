n, c1 , c2 = map(int, input().split())
kabu = [int(input()) for i in range(n)]
price = 0
have = 0
for i in range(0, n):
    if i == n-1:
        price += kabu[n-1] * have
        have = 0    
    elif kabu[i] <= c1:
        price -= kabu[i]
        have += 1
        
    elif kabu[i] >= c2:
        price += kabu[i]* have
        have = 0

print(price)