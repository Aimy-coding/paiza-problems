s= input().split("+")
a =0
for i in range(len(s)):
    a +=s[i].count("<")*10 
    a+= + s[i].count("/")
    
print(a)
