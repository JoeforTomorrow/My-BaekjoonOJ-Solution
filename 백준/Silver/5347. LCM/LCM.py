def my_gcd(x,y):
    if x % y == 0:
        return y
    return my_gcd(y, x%y)

for _ in range(int(input())):
    a, b = map(int,input().split())
    print(int(a*b/my_gcd(a,b)))