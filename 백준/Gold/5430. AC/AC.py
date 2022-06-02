from collections import deque

for _ in range(int(input())):
    txt = input()
    m = int(input())
    arr = input()[1:-1].split(",")
    queue = deque(arr)

    cnt, front, back = 0, 0, len(queue)-1
    res = 0
    if m == 0:
        queue = []
        front = 0
        back = 0

    for j in txt:
        
        if j == 'R':
            cnt += 1
        elif j == 'D':
            if len(queue) < 1:
                res = 1
                print("error")
                break
            else:
                if cnt % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
                    
    if res == 0:
        if cnt % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")