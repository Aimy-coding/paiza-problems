a, b = 0,1
answer = []
result=0

while b < 4000000:
    if b%2 == 0:
        result += b


    a, b = b, a+b
print(result)




