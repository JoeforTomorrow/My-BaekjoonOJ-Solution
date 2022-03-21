A, B, V = map(int,input().split())
height = V - A
if height % (A-B) == 0:
    res = height/(A-B)
else:
    res = height/(A-B) + 1
print(int(res) + 1)