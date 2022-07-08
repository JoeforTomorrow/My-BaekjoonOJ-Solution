import datetime as dt

for _ in range(int(input())):
    start,end = input().split()
    start,end = list(map(int,start.split('/'))),list(map(int,end.split('/')))
    start = [start[2],start[0],start[1]]
    y = start[0]
    if start[1] == 12 and end[0] == 1:
        n = int(f'{(dt.date(start[0],start[1],start[2])-dt.date(start[0]+1,end[0],end[1])).days}'.split()[0])
        y += 1
    elif start[1] == 1 and end[0] == 12:
        n = int(f'{(dt.date(start[0],start[1],start[2])-dt.date(start[0]-1,end[0],end[1])).days}'.split()[0])
        y -= 1
    else:
        n = int(f'{(dt.date(start[0],start[1],start[2])-dt.date(start[0],end[0],end[1])).days}'.split()[0])
    if abs(n) <= 7:
        if n == 0:
            print('SAME DAY')
        elif n < 0:
            if n == -1:
                print(f'{end[0]}/{end[1]}/{y} IS {abs(n)} DAY AFTER')
            else:
                print(f'{end[0]}/{end[1]}/{y} IS {abs(n)} DAYS AFTER')
        else:
            if n == 1:
                print(f'{end[0]}/{end[1]}/{y} IS {abs(n)} DAY PRIOR')
            else:
                print(f'{end[0]}/{end[1]}/{y} IS {abs(n)} DAYS PRIOR')
    else:
        print("OUT OF RANGE")