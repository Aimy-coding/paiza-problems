# one :3
# two :3
# three:5
# four :4
# five :4
# six :3
# seven :5
# eight :5
# nine :4
# ten 3

num0_9 = [0,3, 3, 5, 4, 4, 3, 5, 5, 4]
num10_19 = [3, 6, 6, 8,8,7,7,9,8,8 ]
#Twenty/Thirty/forty/fifty/sixty/seventy/eighty/ninety
num_ty =[0,3,6,6,5,5,5,7,6,6]

hundred = 7
andnum = 3
oneThousand = 11

def numLength(n):
    if 0 < n < 10:
        return (num0_9[n])
    if 10 <= n < 20:
        tmp = int(n % 10)
        return (num10_19[tmp])
    if 20 <= n < 100:
        tenVal = int(n // 10)
        oneVal = int(n % 10)
        return num_ty[tenVal] + num0_9[oneVal]
    if 100 <= n < 1000:
        hunVal = n // 100
        tenVal = int(str(n)[-2])
        oneVal = int(str(n)[-1])
        if n % 100 == 0:
            return num0_9[hunVal] + hundred
        elif tenVal == 1:
            return num0_9[hunVal] + hundred + andnum + num10_19[oneVal]
        else:
            return num0_9[hunVal] + hundred + andnum + num_ty[tenVal] + num0_9[oneVal]
    if n == 1000:
        return oneThousand
print(numLength(8))
num = 1000
count = 0

for i in range(num):
    count += numLength(i+1)
print(count)

