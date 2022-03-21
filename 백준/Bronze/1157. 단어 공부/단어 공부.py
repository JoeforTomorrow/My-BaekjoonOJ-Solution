text = input()
text = text.upper()
dic1 = { i : text.count(i) for i in set(text) }
lst1 = []
for i in dic1:
    if dic1[i] == max(dic1.values()):
        lst1.append(dic1[i])
for i in dic1:
    if dic1[i] == max(dic1.values()):
        if len(lst1) == 1:
            print(i)
            break
        else:
            print("?")
            break