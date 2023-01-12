a = list(map(int, sorted(input().split())))

n = int(input())
s = [list(map(int, sorted(input().split()))) for i in range(n)]

for i in range(n):
    answer = 0
    for i2 in range(len(a)):
        if a[i2] in s[i]:
            answer +=1
    print(answer)
            