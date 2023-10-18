import sys

def rou(n):
	if n - int(n) < 0.5:
		return int(n)
	else:
		return int(n) + 1
n = int(sys.stdin.readline())
if n == 0:
	print(0)
else:
	person = rou(n*0.15)
	score = []
	for _ in range(n):
		score.append(int(sys.stdin.readline()))
	score.sort()
	if person != 0:
		score  = score[person:-person]
	mean = rou(sum(score)/len(score))
	print(mean)