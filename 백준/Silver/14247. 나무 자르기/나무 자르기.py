a=int(input())
lst1=list(map(int,input().split()))
lst2=list(map(int,input().split()))
lst = [True] * a
for i in range(a):
    lst[i] = (lst1[i],lst2[i])
lst = sorted(lst,key=lambda x : x[1])
cnt=0
for i in range(a-1,-1,-1):
    cnt+=lst[i][1]*i+lst[i][0]
print(cnt)