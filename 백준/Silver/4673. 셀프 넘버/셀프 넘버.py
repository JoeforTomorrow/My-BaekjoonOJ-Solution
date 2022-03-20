res = 0
lst1 = list(range(1,10001))
lst2 = []
for i in lst1:
    for j in range(0,len(str(i))):
        res += int(str(i)[j])
    res += i
    lst2.append(res)
    res = 0
set1 = set(lst1)
set2 = set(lst2)
lst3=list(set1.difference(set2))
lst3.sort()
for i in lst3:
    print(i)