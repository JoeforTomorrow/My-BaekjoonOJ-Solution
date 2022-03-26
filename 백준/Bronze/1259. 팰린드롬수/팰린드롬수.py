while True:
    txt_1=input()
    if txt_1 == "0":
        break
    txt_2 = txt_1[::-1]
    if txt_1==txt_2:
        print("yes")
    else:
        print("no")