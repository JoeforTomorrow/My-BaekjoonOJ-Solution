n,k=map(int,input().split())
lst1=list(map(int,input().split(',')))
lst2=[]
for i in range(0,k):
    for j in range(0,len(lst1)-1):
        lst2.append(lst1[j+1]-lst1[j])
    lst1=lst2[:]
    lst2=[]
res=""
for i in range(0,len(lst1)):
    res += f"{lst1[i]},"
print(res.strip(','))