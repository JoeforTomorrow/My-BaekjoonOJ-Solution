import sys
input = sys.stdin.readline
dic = {}
for i in range(int(input())):
    a, b = input().split()
    if b == "enter":
        dic[a] = "enter"
    else:
        if dic[a]:
            del dic[a]
dic = sorted(dic.keys(), reverse=True)
for i in dic:
    print(i)