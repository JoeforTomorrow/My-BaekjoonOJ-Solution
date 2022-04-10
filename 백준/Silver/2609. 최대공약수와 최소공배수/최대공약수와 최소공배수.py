def my_func(x,y):
    if x % y == 0:
        return y
    return my_func(y, x%y)

x, y = map(int,input().split())
print(my_func(x,y),int(x*y/my_func(x,y)),sep='\n')