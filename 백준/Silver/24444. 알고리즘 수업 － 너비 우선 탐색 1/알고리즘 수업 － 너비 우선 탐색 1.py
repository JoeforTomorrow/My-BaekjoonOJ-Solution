from collections import deque
import sys
input = sys.stdin.readline

n,m,start = map(int,input().split())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=1
    cnt=2
    
    while queue:
        start=queue.popleft()
        
        for i in graph[start]:
            if visited[i]==0:
                queue.append(i)
                visited[i]=cnt 
                cnt+=1

visited=[0]*(n+1)

bfs(graph,start,visited)

for i in visited[1::]:
    print(i)
