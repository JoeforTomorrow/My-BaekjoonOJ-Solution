n = input()
lst = list(map(int,input().split()))
res = sorted(list(set(lst)))
dic = {}
for i in range(len(res)):
    dic[res[i]]=i
x = 0
for i in lst:
    print(dic[i],end=' ')