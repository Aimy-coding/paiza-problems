# palindromic number 回文
#失敗
result = []
for i in range(100, 999):
  for j in range(i, 999):
    ans = str(i*j)
    if ans ==  str(ans)[::-1]:
      result.append(i *j)
a = sorted(result)            
print(result[-1]) 

#正解
def is_palindrome(num: int) -> bool:
	num_str = str(num)
	num_len = len(num_str)
	idx = 0
	while idx < num_len:
		if num_str[idx] != num_str[-1 - idx]:
			return False
		idx += 1
	return True

result = 0
count = 0
for i in range(100, 1000):
	for j in range(i, 1000):
		count += 1
		if is_palindrome(i * j):
			result = max(result, i * j)
