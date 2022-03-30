import heapq
import sys
input = sys.stdin.readline

heap = []
for _ in range(int(input())):
    num = int(input())
    if num!=0:
        heapq.heappush(heap, (-num,num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)