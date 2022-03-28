import sys
input = sys.stdin.readline
input()
lst1=list(map(int,input().split()))
input()
lst2=list(map(int,input().split()))

st1=set(lst1)
st2=set(lst2)
res=list(st2.intersection(st1))

for i in lst2:
    if i in res:
        print(1)
    else:
        print(0)