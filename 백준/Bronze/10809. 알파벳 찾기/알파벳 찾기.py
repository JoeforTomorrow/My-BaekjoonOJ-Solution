txt=input()
res=[-1 for i in range(26)]
rep=0
for i in range(len(txt)):
    for j in range(26):
        if txt[i] == chr(rep+97):
            if res[rep] == -1:
                res[rep] = i
        rep+=1
    rep=0
for i in res:
    print(i)