from collections import deque
import sys

input = sys.stdin.readline

parrots = [deque(input().rstrip().split()) for _ in range(int(input()))]

sentence = input().rstrip().split()

removed = []
for word in sentence:
    for i in range(len(parrots)):
        if parrots[i] and word == parrots[i][0]:
            parrots[i].popleft()
            removed.append(word)
            break

for i in range(len(parrots)):
    if parrots[i]:
        print("Impossible")
        exit()
if sentence != removed:
    print("Impossible")
else:
    print("Possible")