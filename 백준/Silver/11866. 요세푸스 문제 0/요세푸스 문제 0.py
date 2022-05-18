from collections import deque
n,k=map(int,input().split())
queue=deque([i for i in range(1,n+1)])
lst=[]
for _ in range(n):
    queue.rotate(-k)
    lst.append(queue[-1])
    queue.pop()

res = "<"
for i in lst:
    if i != lst[-1]:
        res += f"{i}, "
    else:
        res += f"{i}>"

print(res)