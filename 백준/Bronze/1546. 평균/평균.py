n = int(input())
lst1 = list(map(int,input().split()))
score = max(lst1)
lst2 = []
for i in range(0,n):
    lst2.append(lst1[i]/score*100)
print(sum(lst2)/n)