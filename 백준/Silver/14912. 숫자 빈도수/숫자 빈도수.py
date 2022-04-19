a,b=map(int,input().split())
a=list(map(str,range(1,a+1)))
lst=[i.count(str(b)) for i in a if str(b) in str(i)]
print(sum(lst))