import math

# エラトステネスの篩
def prime(n):
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(2 * i, n + 1, i):
                is_prime[j] = False
    return is_prime

# 素数列挙
#N = int(input())
# M以下の整数の素数判定
prime = prime(1000000)

# 素数判定を基に, 素数リストを作成
consecutiveprime = []
primes = []

for i in range(1000000 + 1):
    if prime[i]:
        primes.append(i)
# length of the consecutive prime sum
length = 0

# value of the consecutive prime sum
largest = 0

# max value of the j variable(second for loop)
lastj = len(primes)
# two for loops
#sequence[start : stop : step]
for i in range(len(primes)):
    for j in range(i+length, lastj):
        sol = sum(primes[i:j])
        if sol < 1000000:
            if sol in primes:
                length = j-i
                largest = sol
        else:
            lastj = j+1
            break

# printing the requried solution
print(largest) 
           