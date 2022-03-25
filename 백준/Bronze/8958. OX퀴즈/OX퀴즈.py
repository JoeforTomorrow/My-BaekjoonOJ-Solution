for i in range(int(input())):
    res=0
    plus=1
    x=input()
    for j in range(len(x)):
        if x[j] == "O":
            res += plus
            plus += 1
        else:
            plus = 1
    print(res)
