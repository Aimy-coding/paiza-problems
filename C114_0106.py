n = int(input())
word =  [input() for i in range(n)]
a=0
for i in range(n-1):
    if word[i][-1] != word[i+1][0]:
        print(word[i][-1] + " " +word[i+1][0])
        break
    elif word[i][-1] == word[i+1][0]:
        a+= 1
if a== n-1:
    print("Yes")
