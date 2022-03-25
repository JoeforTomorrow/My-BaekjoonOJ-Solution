dic1 = {}
for i in range(int(input())):
    a = input()
    if a not in dic1.keys():
        dic1[a] = 1
    else:
        dic1[a] += 1
lst = [i for i,j in dic1.items() if max(dic1.values())==j]
lst.sort()
print(lst[0])