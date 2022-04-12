import sys
input = sys.stdin.readline
txt = input()
lst = ['U','C','P','C']
switch = 1

for i in lst:
    if i in txt:
        txt = txt[txt.find(i)+1:]
    else:
        switch = 0
        break

if switch:
    print("I love UCPC")
else:
    print("I hate UCPC")