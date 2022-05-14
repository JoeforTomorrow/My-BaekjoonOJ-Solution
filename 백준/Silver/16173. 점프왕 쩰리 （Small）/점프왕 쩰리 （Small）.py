from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

visited = [[False] * n for _ in range(n)]

dx = [1,0]
dy = [0,1]

def bfs(x, y, visited):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    while queue:
        x,y = queue.popleft()
        if graph[x][y] == -1:
            return "HaruHaru"
        for i in range(2):
            nx = x + dx[i] * graph[x][y]
            ny = y + dy[i] * graph[x][y]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny))
    return "Hing"
    
print(bfs(0,0,visited))