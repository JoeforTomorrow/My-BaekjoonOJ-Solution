import sys
input = sys.stdin.readline
while 1:
    x,y = map(int,input().split())
    if (x,y) != (0,0) :
        lst1 = []
        lst2 = []
        for i in range(x):
            lst1.append(input())
    
        for i in range(y):
            lst2.append(input())
        st1=set(lst1)
        st2=set(lst2)
        print(len(st1.intersection(st2)))
    else:
        break

