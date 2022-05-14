from collections import deque
import sys

input = sys.stdin.readline

n,m,start = map(int,input().split())
visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort(reverse=True)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1
    cnt = 2
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = cnt
                cnt += 1
                
bfs(graph,start,visited)

for i in visited[1:]:
    print(i)