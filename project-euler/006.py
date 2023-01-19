#2520
#naturalnumber 整数
square = 0
sum = 0
for i  in range(1, 101):
    square += i*i
    sum += i
ans = sum * sum - square
print(ans)
