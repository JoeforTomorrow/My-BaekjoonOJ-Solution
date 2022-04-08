while 1:
    txt = input()
    if txt == ".":
        break
    else:
        txt = list(map(str,txt))
        lst = ["a"]
        cnt1 = 0
        cnt2 = 0
        for i in txt:
            if i == "]":
                if lst[-1] == "(":
                    break
                else:
                    pass
                lst.pop()
                cnt1 -= 1
            elif i == "[":
                lst.append("[")
                cnt1 += 1
            elif i == ")":
                if lst[-1] == "[":
                    break
                else:
                    pass
                lst.pop()
                cnt2 -= 1
            elif i == "(":
                lst.append("(")
                cnt2 += 1
            else:
                pass
            if cnt1 < 0 or cnt2 < 0:
                break
        if cnt1 == 0 and cnt2 == 0:
            print("yes")
        else:
            print("no")

