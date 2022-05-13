from collections import deque
import sys
input = sys.stdin.readline

N,M,R = map(int,sys.stdin.readline().split())

graph=[[] for _ in range(N+1)]

for i in range(M):
    tmpL=list(map(int,sys.stdin.readline().split()))
    graph[tmpL[0]].append(tmpL[1])
    graph[tmpL[1]].append(tmpL[0])

for i in range(N+1):
    graph[i].sort()

def bfs(graph,R,visited):
    queue=deque([R])
    visited[R]=1
    count=2
    
    while queue:
        R=queue.popleft()
        
        for i in graph[R]:
            if visited[i]==0:
                queue.append(i)
                visited[i]=count 
                count+=1

visited=[0]*(N+1)

bfs(graph,R,visited)

for i in visited[1::]:
    print(i)