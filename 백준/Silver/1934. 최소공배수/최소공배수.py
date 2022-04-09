def my_func(x,y):
    if x % y == 0:
        return y
    return my_func(y, x%y)

for i in range(int(input())):
    x, y = map(int,input().split())
    print(int(x*y/my_func(x,y)))