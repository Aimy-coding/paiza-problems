a, b = map(int, input().split())
al = list()
for x in range(1, 10):
    for y in range(10):
        if (10*x + y) * y == 100*a + 10*x + b:
            al.append([x, y])
if len(al) == 0:
    print('No')
else:
    print(f'{al[0][0]} {al[0][1]}')