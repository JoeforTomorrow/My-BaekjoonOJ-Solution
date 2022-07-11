txt = input().split('-')
for i in range(len(txt)):
    txt[i] = sum(list(map(int,txt[i].split('+'))))
res = txt[0]
for n in txt[1:]:
    res -= n
print(res)