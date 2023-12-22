N,M = map(int,input().split())
board = []
result = []
for i in range (N):
	board.append(input())
for i in range (N - 7):
	for j in range(M - 7):
		w = 0
		b = 0
		for k in range (i, i +8):
			for l in range(j, j +8):
				if (k+l)%2 == 0:
					if (board[k][l] != 'W'):
						w+=1
					if (board[k][l] != 'B'):
						b+=1
				else:
					if (board[k][l] != 'W'):
						w+=1
					if (board[k][l] != 'B'):
						b+=1
		result.append(w)
		result.append(b)
print(min(result))