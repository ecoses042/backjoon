K,N = map(int,input().split())
son = [K]
for i in range(K):
	son.append(int(input()))
min = 1
max = max(son)
while min <= max:
	mid = (min+max)//2
	count = 0
	for j in son:
		count += j // mid
	if count >= N:#정답보다 짧게 잘랐을 때
		min = mid + 1
	else: #정답보다 길게 잘랐을 때
		max = mid - 1
print(max)