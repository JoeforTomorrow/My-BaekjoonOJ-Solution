for _ in range(int(input())):
    txt = list(map(str,input()))
    cnt = 0
    if txt[0] == "(":
        cnt += 1
        for i in txt[1:]:
            if cnt < 0:
                break
            else:
                pass
            if i == "(":
                cnt += 1
            else:
                cnt -= 1
        if cnt == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
