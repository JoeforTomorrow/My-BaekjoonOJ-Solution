n,m = map(int,input().split())
r,c,d = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
visited[r][c] = 1
cnt = 1

dr = [-1,0,1,0]
dc = [0,1,0,-1]
while True:
    is_not_clean = False
    for _ in range(4):
        d = (d+3) % 4 
        nr = dr[d] + r
        nc = dc[d] + c
        if 0 <= nr < n and 0 <= nc < m and matrix[nr][nc] == 0 and visited[nr][nc] == 0:
            is_not_clean = True
            break
    if is_not_clean:
        visited[nr][nc] = 1
        cnt += 1
        r,c = nr,nc
    else:
        if matrix[r-dr[d]][c-dc[d]] == 1:
            print(cnt)
            break
        else:
            r,c = r-dr[d], c-dc[d]