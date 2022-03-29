import sys
input = sys.stdin.readline
int(input())
res = []
lst_1 = list(map(int,input().split()))
lst_2 = list(map(int,input().split()))
lst_1.sort()
lst_2.sort(reverse=True)
for j,k in zip(lst_1,lst_2):   
    res.append(j*k)
print(sum(res))