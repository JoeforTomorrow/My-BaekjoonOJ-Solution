txt=sorted(list(input()))
check=list(set(txt))
res=0
cen=""
for i in check:
    if txt.count(i)%2 != 0:
        res+= 1
        cen += i
if res > 1:
    print("I'm Sorry Hansoo")
else:
    lst=list(txt)
    if cen in lst:
        lst.remove(cen)
    txt1=""
    for i in lst[::2]:
        txt1+=i
    print(txt1,cen,txt1[::-1],sep="")