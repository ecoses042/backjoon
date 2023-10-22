<<<<<<< HEAD
from collections import deque

m,n = map(int,input().split())
matrix = [list(input().split()) for _ in range(m)]
queue = deque([])
visited = [[0]*n for _ in range(m)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
#m = 3, n = 5
for i in range(m):
    for j in range(n):
        if matrix[i][j] == "I":
            queue.append([i,j])
            visited[i][j] = 1

def bfs():
    person = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == "P" and visited[nx][ny] != 1:
                    person += 1
                    queue.append([nx,ny])
                    visited[nx][ny] == 1
                if matrix[nx][ny] == "O" and visited[nx][ny] != 1:
                    queue.append([nx,ny])
                    visited[nx][ny] == 1
    return person
people = bfs()
if people == 0:
    print("TT")
else:
    print(people)
                
                    
=======
from collections import deque

m,n = map(int,input().split())
matrix = [list(input().split()) for _ in range(m)]
queue = deque([])
visited = [[0]*n for _ in range(m)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
#m = 3, n = 5
for i in range(m):
    for j in range(n):
        if matrix[i][j] == "I":
            queue.append([i,j])
            visited[i][j] = 1

def bfs():
    person = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == "P" and visited[nx][ny] != 1:
                    person += 1
                    queue.append([nx,ny])
                    visited[nx][ny] == 1
                if matrix[nx][ny] == "O" and visited[nx][ny] != 1:
                    queue.append([nx,ny])
                    visited[nx][ny] == 1
    return person
people = bfs()
if people == 0:
    print("TT")
else:
    print(people)
                
                    
>>>>>>> 511266efab99ac67ff8bdfcad871a8e101b4458e
