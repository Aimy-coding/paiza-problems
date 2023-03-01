n, x = map(int, input().split())
change= str(format(x, "b"))
newlist = list(reversed(change))
#print(newlist)    
for i in range(n):
    s = int(input())-1
    
    print(int(newlist[s]))
    