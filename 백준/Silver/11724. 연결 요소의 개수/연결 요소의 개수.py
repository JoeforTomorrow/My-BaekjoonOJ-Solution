import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph,start,visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for j in graph[v]:
            if not visited[j]:
                queue.append(j)
                visited[j] = True

n,m=map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()

cnt = 0            
for i in range(1, n+1):
    if not visited[i]:
        bfs(graph,i,visited)
        cnt += 1

print(cnt)