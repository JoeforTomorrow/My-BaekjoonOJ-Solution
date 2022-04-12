import sys
input = sys.stdin.readline
cnt = 1
while 1:
    L,P,V=map(int,input().split())
    if (L,P,V) == (0,0,0):
        break
    if V%P >= L:
        res = V//P * L + L
    else:
        res = V//P * L + V%P
    print(f"Case {cnt}: {res}")
    cnt += 1