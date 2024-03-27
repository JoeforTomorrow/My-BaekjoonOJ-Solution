from collections import deque

n,m = map(int,input().split())
# ladders, snakes = {}, {}
jump = {}
for _ in range(n+m):
    a,b = map(int,input().split())
    jump[a] = b

board = [0] * 101
visited = [False] * 101

q = deque([1])

while q:
    place = q.popleft()
    visited[place] = True
    if place == 100:
        print(board[place])
        break
    for dice in range(1,7):
        new_place = place + dice
        if new_place <= 100 and not visited[new_place]:
            new_place = jump.get(new_place, new_place)
            if not visited[new_place]:
                visited[new_place] = True
                board[new_place] = board[place] + 1
                q.append(new_place)