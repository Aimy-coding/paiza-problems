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
prime = prime(9999)

# 素数判定を基に, 素数リストを作成

primes = []
##二つの数が並び替えで同じになるかチェック
def isPermSame(n1, n2):
  return ("".join(sorted(str(n1)))) == ("".join(sorted(str(n2))))

for i in range(1000,9999 + 1):
    if prime[i]:
        primes.append(i)

for i in range(len(primes)):
    for inc in range(2, 5000):
        p1, p2 = primes[i]+inc, primes[i] + 2*inc

        if p2 < 10000 and primes[i] != 1487 and \
           p2 in primes and p1 in primes and \
           isPermSame(primes[i], p1) and isPermSame(primes[i], p2):
            
           ans = "".join([str(primes[i]), str(p1), str(p2)])
print(ans)
    