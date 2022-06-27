import sys

input = sys.stdin.readline

dic = {}
for i in range(int(input())):
    txt = f'{sorted(list(map(str,input())))}'
    if txt not in dic:
        dic[txt] = 0
    else:
        dic[txt] += 1
print(len(dic))