n = int(input())
dic = {}

for i in range(n):
    txt = input().split('.')[1]
    if txt not in dic:
        dic[txt] = 1
    else:
        dic[txt] += 1
        
lst = sorted(dic.items())

for i in lst:
    print(i[0],i[1])