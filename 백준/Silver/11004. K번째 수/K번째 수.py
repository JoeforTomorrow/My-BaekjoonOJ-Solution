a,b=map(int,input().split())
lst=list(map(int,input().split()))
lst.sort()
print(lst.pop(b-1))