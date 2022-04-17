lst = []
for i in range(int(input())):
    lst.append(int(input()))
lst.sort()
a=(max([-lst[0]+2*lst[i]-lst[i+1] for i in range(1,len(lst)-1)]))
b=(max([lst[-1]-2*lst[i]+lst[i-1] for i in range(1,len(lst)-1)]))
print(max(a,b))