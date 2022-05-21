import sys
input = sys.stdin.readline
n,m=map(int,input().split())
dic={}
for _ in range(n):
    dic[input()] = 0
for _ in range(m):
    txt = input()
    if txt in dic:
        dic[txt] += 1
    else:
        pass
print(sum(dic.values()))