from collections import deque

def bfs(graph, start, visited):
    lst = 0
    queue=deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                lst += 1
    return lst

n = int(input())
m = int(input())

visited=[False]*(n+1)

graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()


a=bfs(graph, 1, visited)
print(a)