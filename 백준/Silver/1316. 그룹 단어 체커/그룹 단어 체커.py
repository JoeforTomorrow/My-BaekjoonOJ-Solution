import sys
rep = int(sys.stdin.readline())
res = 0
for _ in range(rep):
    txt = sys.stdin.readline()
    for i in txt:
        if txt.count(i) * i in txt:
            pass
        else:
            rep -= 1
            break
print(rep-res)