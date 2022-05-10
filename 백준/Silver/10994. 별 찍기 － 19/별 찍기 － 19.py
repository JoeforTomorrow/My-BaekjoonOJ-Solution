n = int(input())
stars = [[' ' for _ in range(4*n-3)] for _ in range(4*n-3)]

def star_cnt(n,x,y):
    if n == 1:
        stars[y][x]="*"
        return
    length = 4*n-3
    for i in range(length):
        stars[y][x+i] = '*'
        stars[y+i][x] = "*"
        stars[y+length-1][x+i]='*'
        stars[y+i][x+length-1]="*"
    star_cnt(n-1,x+2,y+2)
star_cnt(n,0,0)
for i in stars:
    for j in i:
        print(j,end='')
    print("")