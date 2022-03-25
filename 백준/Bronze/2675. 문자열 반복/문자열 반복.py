for i in range(int(input())):
    a,b=input().split()
    a=int(a)
    res = ''
    for i in range(len(b)):
        res += b[i]*a
    print(res)