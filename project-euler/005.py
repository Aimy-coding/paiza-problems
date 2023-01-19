#2520
#remainder あまり
num = 2520 
i =2 
while i < 21:
    if num % i  == 0:
        check = 'good'
        i = i +1
    else:
        num = num+1
        i = 2
print(num)
