N = int(input())
p = list(map(int,input().split()))
count = 0
sum = 0
p.sort()
for _ in range(N):
	count +=p[0]
	sum += count
	del p[0]
print(sum)