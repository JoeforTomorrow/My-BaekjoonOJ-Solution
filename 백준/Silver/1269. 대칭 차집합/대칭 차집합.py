input()
st1=set(map(int,input().split()))
st2=set(map(int,input().split()))
print(len(st1.difference(st2))+len(st2.difference(st1)))