d = {}
maxtime = 0
maxnum = 0

def calculation(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

for i in range(1, 1000000):
    a = i
    count = 0
    while True:
        if a in d:
            times = count + d[a]
            d[i] = times
            if times > maxtime:
                maxtime = times
                maxnum = i
            break
        elif a == 1:
            d[i] = count + 1
            if count + 1 > maxtime:
                maxtime = count + 1
                maxnum = i
            break
        else:
            a = calculation(a)
            count += 1

print(maxnum)
