from collections import deque

n,m = map(int, input().split())

graph = [list(map(int, input().split())) for i in range(m)]

dx = [1,-1,0,0]
dy = [0,0,-1,1]

q = deque()

for x in range(n):
    for y in range(m):
        if graph[y][x] == 1:
            q.append([x,y])

while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[ny][nx] == 0:
            graph[ny][nx] = graph[y][x] + 1
            q.append([nx,ny])

max_value = 0
flag = False
for x in range(n):
    for y in range(m):
        max_value = max(max_value, graph[y][x])
        if graph[y][x] == 0:
            flag = True

if flag:
    print(-1)
else:
    print(max_value-1)