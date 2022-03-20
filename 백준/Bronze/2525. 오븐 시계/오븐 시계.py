h,m=map(int,input().split())
r = int(input())
time = h * 60 + m + r
if time//60 >= 24:
    print(time//60 - 24, time%60)
else:
    print(time//60, time%60)