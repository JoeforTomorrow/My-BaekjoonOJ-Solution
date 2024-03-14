from collections import deque


def dfs(graph, v, visited, dfs_res):
    visited[v] = True
    dfs_res.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited, dfs_res)
    return dfs_res

def bfs(graph, start, visited, bfs_res):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        bfs_res.append(v)
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    return bfs_res

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for node in graph:
    node.sort()

dfs_res = []
bfs_res = []
visited = [False] * (n+1)
d = dfs(graph,v,visited,dfs_res)
visited = [False] * (n+1)
b = bfs(graph,v,visited,bfs_res)
print(*d)
print(*b)