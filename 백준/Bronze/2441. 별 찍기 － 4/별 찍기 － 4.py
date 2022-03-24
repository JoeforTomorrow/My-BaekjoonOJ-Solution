a=int(input())
j=0
for i in range(0,a):
    if j == 0:
        print("*"*(a-i))
    else:
        print(f'{" "*i}{"*"*(a-i)}')
    j += 1