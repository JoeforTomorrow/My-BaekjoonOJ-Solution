import sys

input = sys.stdin.readline

def my_func(x,y):
    if x % y == 0:
        return y
    return my_func(y, x%y)

for _ in range(int(input())):
    lst = list(map(int,input().split()))[1:]
    lst.sort(reverse=True)
    res = 0
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            res += my_func(lst[i],lst[j])
    print(res)