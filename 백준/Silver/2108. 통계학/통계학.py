import sys
import statistics as stt
input = sys.stdin.readline
n = int(input())
lst = []

for i in range(n):
    k = int(input())
    lst.append(k)

lst.sort()
mode = stt.multimode(lst)
mode.sort()
print(round(stt.mean(lst)),stt.median(lst),mode[1] if len(mode) > 1 else mode[0],max(lst)-min(lst),sep="\n")