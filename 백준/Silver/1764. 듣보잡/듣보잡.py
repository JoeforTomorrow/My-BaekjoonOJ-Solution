a,b = map(int,input().split())
lst_a=[]
lst_b=[]
for i in range(a):
    lst_a.append(input())
for i in range(b):
    lst_b.append(input())
st_a = set(lst_a)
st_b = set(lst_b)
st_c = (st_a & st_b)
print(len(st_c))
lst_c = list(st_c)
lst_c.sort()
for i in lst_c:
    print(i)