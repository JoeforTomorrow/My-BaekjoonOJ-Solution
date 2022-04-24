from collections import Counter
import sys
input = sys.stdin.readline

marathoners = Counter()
n = int(input())
for i in range(2*n-1):
    player = input()
    if marathoners[player] not in marathoners:
        marathoners[player]+=1
for i in marathoners.items():
    if i[1]%2 == 1:
        print(i[0])