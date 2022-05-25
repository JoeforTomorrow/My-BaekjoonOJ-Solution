txt = input()
res=[]
for i in range(len(txt)):
    for j in range(i+1,len(txt)+1):
        res.append(txt[i:j])
print(len(set(res)))