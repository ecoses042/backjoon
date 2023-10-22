import math

n = int(input())
n -= 1
for k in range(1, n + 1):
	if n == k + k ** 2:
		print(k)
		break