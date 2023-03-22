def yakusu(N):
    Answer = []
    LIMIT = int(N ** 0.5)
    for i in range(2, LIMIT + 1):
        while N % i == 0:
            N /= i
            Answer.append(i)

    if N >= 2:
        Answer.append(int(N))

    # 出力
 ##   print(len(Answer))
    return Answer
n = 5
from collections import Counter
# collectionsの使い方https://www.sejuku.net/blog/28832
#Counterの戻り値は、引数に設定したコンテナ型の要素とその数を格納した辞書形に似た形で返ってきます。
while True:
    #三角数にした
    num = n * (n+1)/2
    #ディクショナリにした
    c = Counter(yakusu(num))
    print(c)
    
    index_list = list(c.values())
    print(c.values)
    print(index_list)
    num_of_divisors = 1
    
    #divisor 除数
    for i in index_list:
        num_of_divisors *= (i+1)
        print(num_of_divisors)
    if num_of_divisors >= 500:
        break
    else:
        n += 1
        continue
print(num)