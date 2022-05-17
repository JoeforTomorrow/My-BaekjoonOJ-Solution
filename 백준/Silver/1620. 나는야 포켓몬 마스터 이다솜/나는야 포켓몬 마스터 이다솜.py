n,m=map(int,input().split())
poke_dic={}
for i in range(1,n+1):
    poke_dic[i]=input()
reverse_dic=dict(map(reversed,poke_dic.items()))
res = []
for _ in range(m):
    fnd=input()
    try:
        res.append(poke_dic[int(fnd)])
    except:
        res.append(reverse_dic[fnd])
for i in res:
    print(i)