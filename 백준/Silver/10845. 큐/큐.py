from collections import deque
import sys

input = sys.stdin.readline

queue = deque([])

for i in range(0,int(input())):
    a = input()
    if "push" in a:
        queue.append(int(a[5:]))
    elif "pop" in a:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif "size" in a:
        print(len(queue))   
    elif "empty" in a:
        if len(queue) == 0:
            print(1)
        else:
            print(0)   
    elif "front" in a:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])   
    elif "back" in a:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])   