h,m=map(int,input().split())
time = h * 60 + m - 45
if time//60 < 0:
    print(time//60 + 24, time%60)
else:
    print(time//60, time%60)