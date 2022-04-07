a=input()
b=a
cnt=0
while len(b)!=1:
    lst=list(map(int,b))
    b=str(sum(lst))
    cnt += 1
print(cnt)
print("YES") if int(a)%3 == 0 else print("NO")