def my_gcd(x,y):
    if x % y == 0:
        return y
    return my_gcd(y, x%y)

for i in range(int(input())):
    lst = list(map(int,input().split()))
    res = []
    for j in range(len(lst)):
        if j < len(lst):
            for k in range(len(lst)):
                if j != k:
                    res.append(my_gcd(lst[j],lst[k]))
    print(max(res))