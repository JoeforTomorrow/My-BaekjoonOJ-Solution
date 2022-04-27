import sys
import re
input = sys.stdin.readline
lst = []
for i in range(int(input())):
    txt=input()
    txt=(re.sub('[a-zA-Z]',' ',txt))
    lst.append(txt)
res = []
for i in lst:
    for j in list(map(str,i.split())):
        res.append(int(j))
res.sort()
for i in res:
    print(i)