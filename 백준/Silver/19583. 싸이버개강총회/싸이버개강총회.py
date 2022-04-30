import sys
input=sys.stdin.readline
n,m,l=map(int,input().replace(":","").split())
cnt=0
grp={}
res={}
while 1:
    try:
        y,x=input().split()
        y=int(y.replace(":",""))
        if x not in grp:
            if y <= n:
                grp[x]=1
        else:
            if (y >= m) and (y <= l):
                cnt+=1
                res[x]=1
    except:
        break
print(len(res))