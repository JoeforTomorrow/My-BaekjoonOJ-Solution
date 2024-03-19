# import sys
from collections import deque

# input = sys.stdin.readline

n = int(input())

matrix = [list(map(int, list(input()))) for _ in range(n)]

def bfs(x,y):
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    q = deque()
    q.append((x,y))
    matrix[x][y] = 0
    cnt = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if n > nx >= 0 and n > ny >= 0:
                if matrix[nx][ny] == 1:
                    q.append((nx,ny))
                    cnt += 1
                    matrix[nx][ny] = 0
    return cnt

cp = 0
lst = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            cp += 1
            lst.append(bfs(i,j))

lst.sort()

print(cp)
print(*lst, sep='\n')