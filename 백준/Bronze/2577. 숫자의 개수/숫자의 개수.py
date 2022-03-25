n=1
for i in range(0,3):
    n*=int(input())
n=str(n)
for i in range(0,10):
    print(n.count(str(i)))