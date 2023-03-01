a, op, b,f,c = map(str, input().split())

if a =="x" and op == "+":
    ans = int(c)-int(b)
if a == "x" and op =="-":
    ans = int(c) + int(b)
if b == "x" and op == "+":
    ans = int(c)-int(a) 
if b == "x" and op == "-":
    ans = int(a)-int(c) 
if c == "x" and op == "+":
    ans = int(a)+ int(b)
elif c == "x" and op == "-":
    ans = int(a)-int(b)
print(ans)
