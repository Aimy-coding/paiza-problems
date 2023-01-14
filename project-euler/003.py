#prime factor 素因数分解
ans =[]
n= 600851475143

f = 3
while f * f <= n:
    if n % f == 0:
        ans.append(f)
        n //=f   #n = n // f に同じ 10//3 = 3
    else:
        f +=2
if n != 1:
    ans.append(n)
print(sorted(ans, reverse=True))



