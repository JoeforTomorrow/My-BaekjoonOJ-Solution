for i in range(int(input())):
    a,b,c = map(int,input().split())

    if c % a != 0:
        d = str((c//a)+1)
        e = str(c%a)
        if int(d) < 10:
            d = "0" + d
        print(e+d)

    else:
        d = str(c//a)
        e = str(a)
        if int(d) < 10:
            d = "0" + d
        print(e+d)