n = int(input())

lst = [0] * n
lst[0],lst[1] = 1,1
for i in range(2,2+len(lst[2:])):
    lst[i] = lst[i-1] + lst[i-2]

print(lst[-1], n-2)