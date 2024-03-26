from collections import deque

n,m = map(int, input().split())

ladders = {}
snakes = {}

for _ in range(n):
    a,b = map(int,input().split())
    ladders[a] = b

for _ in range(m):
    a,b = map(int,input().split())
    snakes[a] = b

graph = [0] * 101
visited = [False] * 101

q = deque([1])

while q:
    place = q.popleft()
    if place == 100:
        print(graph[place])
        break
    for dice in range(1, 7):
        next_place = place + dice
        if next_place <= 100 and not visited[next_place]:
            next_place = ladders.get(next_place) or snakes.get(next_place) or next_place
            if not visited[next_place]:
                visited[next_place] = True
                graph[next_place] = graph[place] + 1
                q.append(next_place)