import sys
lst = []
for i in range(int(input())):
    lst.append(list(map(int,input().split())))
lst.sort()
lst.sort(key=lambda x : x[-1])
for i in lst:
    print(i[0],i[1])