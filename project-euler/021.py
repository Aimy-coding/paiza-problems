def yakusu(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
print(yakusu(220))
print(sum(yakusu(220)), "ans")
data = {}
numMax = 10000
ans = 0
print(yakusu(220)[:-1],"try")

for i in range(numMax):
    division = yakusu(i)[:-1]
    sum_of_yakusu = sum(division)
    data[i] = sum_of_yakusu
    if i != sum_of_yakusu and (sum_of_yakusu, i) in data.items():
        ans += (i + sum_of_yakusu)
        print([i, sum_of_yakusu])
print(ans, "answer")
# print(data)

