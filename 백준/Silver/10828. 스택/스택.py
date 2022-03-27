import sys

lst = []

for i in range(int(sys.stdin.readline())):
    x = sys.stdin.readline()
    if "push" in x:
        lst.append(int(x[5:]))
    elif "top" in x:
        print(lst[-1]) if len(lst) != 0 else print(-1)
    elif "size" in x:
        print(len(lst))
    elif "empty" in x:
        print(1) if len(lst)==0 else print(0)
    elif "pop" in x:
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])
            lst.pop()