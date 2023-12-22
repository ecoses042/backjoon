N = int(input())
count = 0
goal = list(map(int,input().split()))
current = [0] * N

for i in range(N):
    if goal[i] != current[i]:
        count += 1
        current[i] = not current[i]
        if i+1 < N:
            current[i + 1] = not current[i + 1]
        if i+2 < N:
            current[i + 2] = not current[i + 2]
print(count)

