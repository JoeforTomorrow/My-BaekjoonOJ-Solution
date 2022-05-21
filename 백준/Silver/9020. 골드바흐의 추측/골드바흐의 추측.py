n=10000
lst = [False, False] + [True] * (n+1)
res=[]
for i in range(2,n+1):
  if lst[i]:
    res.append(i)
    for j in range(2*i, n+1, i):
        lst[j] = False
   
for i in range(int(input())): 
    n=int(input())

    a=int(n/2)
    b=int(n/2)

    for k in range(int(n/2)):
        if (a in res) and (b in res):
            print(a,b)
            break
        else:
            a=a-1
            b=b+1