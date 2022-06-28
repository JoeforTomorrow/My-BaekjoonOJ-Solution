def my_func(x,y):
    if x % y == 0:
        return y
    return my_func(y, x%y)

x,y = map(int,input().split(':'))
z = my_func(x,y)

print(f'{x//z}:{y//z}')