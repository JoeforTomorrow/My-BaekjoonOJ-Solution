for i in range(int(input())):
    cry = list(input().split())
    rm_cry = []
    while 1:
        txt = list(input().split())
        if txt[1] == "goes":
            rm_cry.append(txt[2])
        else:
            break
    for j in cry:
        if j not in rm_cry:
            print(j,end=' ')