#計算量overしたため動かない
limit = 1000000
ans =[]
for i in range(2, limit):
    if i % 2 != 0: 
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            ans.append(i)
print(ans[10001])

###############
#import sympy
#print(sympy.prime(10001))


#素数判定では、「合成数 x は p≤√x を満たす素因子 p をもつ」という性質を利用
import math

def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    #Math.floor() 関数は与えられた数値以下の最大の整数を返します
    sqrtNum = math.floor(math.sqrt(num))#Math.sqrt() 関数は、ある数の平方根を返します
    for i in range(3, sqrtNum + 1, 2):
        if num % i == 0:
            return False
    
    return True

def find_prime(nth):
	num = 1
	primes = []
	while len(primes) < nth:
		num += 1
		is_prime = True
		for p in primes:
			if num % p == 0:
				is_prime = False
				break
		if is_prime:
			primes.append(num)
	return num
print(find_prime(10001))
