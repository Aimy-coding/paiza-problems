n = 100

nResult = 1
result = 0

for i in range(1, 100+1):
    nResult *= i

nResult = str(nResult)
ans2 = sum(map(int,str(nResult)))


print(ans2)


import math
 
num = math.factorial(100)
print(num)
ans = sum(map(int,str(num)))
print(ans)
