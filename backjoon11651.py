N = int(input())
num = []
for i in range(N):
	num.append(list(map(int,input().split())))
num.sort(key = lambda x:(x[1],x[0]))
for j in num:
	print(j[0],j[1])