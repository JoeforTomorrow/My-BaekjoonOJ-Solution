n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for node in graph:
    node.sort()
visited = [False] * (n+1)
res = []
def dfs(graph, start, visited, res):
    # v = graph[start]
    visited[start] = True
    res.append(start)
    for i in graph[start]:
        # print(graph[start])
        if not visited[i]:
            dfs(graph, i, visited, res)
    return res

r = dfs(graph,1,visited,res)
print(len(r)-1)