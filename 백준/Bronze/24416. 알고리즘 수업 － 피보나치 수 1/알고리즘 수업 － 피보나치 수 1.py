n = int(input())
r,a,b = 0,1,1
for i in range(n-2):
    r = a+b
    a = b
    b = r
print(r, n-2)