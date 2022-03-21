n = int(input())
lst = []
for i in range(0,n):
    lst.append(int(input()))
lst.sort()
for i in range(0,len(lst)):
    print(lst[i])