lst = []

for i in range(int(input())):
    txt = input()
    if txt not in lst:
        lst.append(txt)

lst.sort()
lst.sort(key=lambda x: len(x))

for i in lst:
    print(i)