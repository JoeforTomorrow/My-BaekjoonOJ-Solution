a,b=input().split()
lst_a=list(a)
lst_b=list(b)
lst_a.reverse()
lst_b.reverse()
a1,b1='',''
for i,j in zip(lst_a,lst_b):
    a1 += str(i)
    b1 += str(j)
a1=int(a1)
b1=int(b1)
print(max(a1, b1))