import sys
lst=[]
for i in range(int(sys.stdin.readline())):
    lst.append(int(sys.stdin.readline()))
lst.sort()
for i in lst:
    print(i)