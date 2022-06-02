import sys

input = sys.stdin.readline

n,m = map(int,input().split())
lst = []

for _ in range(n):
    lst.append(list(map(int,input().split())))
    
res = 0
cnt = 0

for i in range(n-1):
    cnt = 0
    for j in range(m-1):
        cnt += lst[i][j]
        cnt += lst[i][j+1]
        cnt += lst[i+1][j]
        cnt += lst[i+1][j+1]
        res = max(cnt,res)
        cnt = 0

for i in range(n):
    for j in range(m-3):
        cnt += lst[i][j]
        cnt += lst[i][j+1]
        cnt += lst[i][j+2]
        cnt += lst[i][j+3]
        res = max(cnt,res)
        cnt = 0

for i in range(n-3):
    cnt = 0
    for j in range(m):
        cnt += lst[i][j]
        cnt += lst[i+1][j]
        cnt += lst[i+2][j]
        cnt += lst[i+3][j]
        res = max(cnt,res)
        cnt = 0
        
        ###
        
for i in range(n-1):
    for j in range(m-2):
        cnt += lst[i][j]
        cnt += lst[i][j+1]
        cnt += lst[i][j+2]
        cnt += lst[i+1][j+1]
        res = max(cnt,res)
        cnt = 0
        
for i in range(n-1):
    for j in range(m-2):
        cnt += lst[i][j]
        cnt += lst[i][j+1]
        cnt += lst[i][j+2]
        cnt += lst[i+1][j+2]
        res = max(cnt,res)
        cnt = 0
        
for i in range(n-1):
    for j in range(m-2):
        cnt += lst[i][j]
        cnt += lst[i][j+1]
        cnt += lst[i][j+2]
        cnt += lst[i+1][j]
        res = max(cnt,res)
        cnt = 0

        ###
        
for i in range(n-1):
    for j in range(m-2):
        cnt += lst[i][j]
        cnt += lst[i+1][j+1]
        cnt += lst[i+1][j+2]
        cnt += lst[i+1][j]
        res = max(cnt,res)
        cnt = 0
        
for i in range(n-1):
    for j in range(m-2):
        cnt += lst[i+1][j]
        cnt += lst[i][j+1]
        cnt += lst[i+1][j+2]
        cnt += lst[i+1][j+1]
        res = max(cnt,res)
        cnt = 0
        
for i in range(n-1):
    for j in range(m-2):
        cnt += lst[i][j+2]
        cnt += lst[i+1][j+1]
        cnt += lst[i+1][j+2]
        cnt += lst[i+1][j]
        res = max(cnt,res)
        cnt = 0
        
###

for i in range(n-2):
    for j in range(m-1):
        cnt += lst[i][j]
        cnt += lst[i+1][j]
        cnt += lst[i+2][j]
        cnt += lst[i][j+1]
        res = max(cnt,res)
        cnt = 0
        
for i in range(n-2):
    for j in range(m-1):
        cnt += lst[i][j]
        cnt += lst[i+1][j]
        cnt += lst[i+2][j]
        cnt += lst[i+1][j+1]
        res = max(cnt,res)
        cnt = 0
        
for i in range(n-2):
    for j in range(m-1):
        cnt += lst[i][j]
        cnt += lst[i+1][j]
        cnt += lst[i+2][j]
        cnt += lst[i+2][j+1]
        res = max(cnt,res)
        cnt = 0
###
for i in range(n-2):
    for j in range(m-1):
        cnt += lst[i][j]
        cnt += lst[i][j+1]
        cnt += lst[i+1][j+1]
        cnt += lst[i+2][j+1]
        res = max(cnt,res)
        cnt = 0
        
for i in range(n-2):
    for j in range(m-1):
        cnt += lst[i][j+1]
        cnt += lst[i+1][j]
        cnt += lst[i+1][j+1]
        cnt += lst[i+2][j+1]
        res = max(cnt,res)
        cnt = 0
        
for i in range(n-2):
    for j in range(m-1):
        cnt += lst[i][j+1]
        cnt += lst[i+1][j+1]
        cnt += lst[i+2][j]
        cnt += lst[i+2][j+1]
        res = max(cnt,res)
        cnt = 0
###
for i in range(n-2):
    for j in range(m-1):
        cnt += lst[i][j]
        cnt += lst[i+1][j]
        cnt += lst[i+1][j+1]
        cnt += lst[i+2][j+1]
        res = max(cnt,res)
        cnt = 0
for i in range(n-2):
    for j in range(m-1):
        cnt += lst[i+1][j]
        cnt += lst[i+1][j+1]
        cnt += lst[i+2][j]
        cnt += lst[i][j+1]
        res = max(cnt,res)
        cnt = 0
###
for i in range(n-1):
    for j in range(m-2):
        cnt += lst[i][j]
        cnt += lst[i][j+1]
        cnt += lst[i+1][j+1]
        cnt += lst[i+1][j+2]
        res = max(cnt,res)
        cnt = 0
for i in range(n-1):
    for j in range(m-2):
        cnt += lst[i+1][j]
        cnt += lst[i+1][j+1]
        cnt += lst[i][j+1]
        cnt += lst[i][j+2]
        res = max(cnt,res)
        cnt = 0
        
print(res)