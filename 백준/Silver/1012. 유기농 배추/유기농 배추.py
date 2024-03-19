import sys
from collections import deque

input = sys.stdin.readline

def bfs(x,y):
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]

    q = deque()
    q.append((x,y))
    matrix[x][y] = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if m > nx >= 0 and n > ny >= 0:
                if matrix[nx][ny]==1:
                    q.append((nx,ny))
                    matrix[nx][ny] = 0

t = int(input())
for _ in range(t):
    m,n,k = map(int, input().split())
    matrix = [[0 for i in range(n)] for _ in range(m)]

    for _ in range(k):
        x,y = map(int, input().split())
        matrix[x][y] = 1

    cnt = 0
    for a in range(m):
        for b in range(n):
            if matrix[a][b] == 1:
                bfs(a,b)
                cnt +=1
                
    print(cnt)