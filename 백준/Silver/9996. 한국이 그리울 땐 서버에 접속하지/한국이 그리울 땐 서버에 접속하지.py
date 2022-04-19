import re
import sys
input=sys.stdin.readline
n=int(input())
condition=list(input().split("*"))
for i in range(n):
    txt=input()
    if txt in re.findall(f"{condition[0]}[a-z]*{condition[1]}",txt):
        print("DA")
    else:
        print("NE")