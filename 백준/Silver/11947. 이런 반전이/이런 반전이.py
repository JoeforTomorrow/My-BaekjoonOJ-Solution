for i in range(int(input())):
    txt=input()
    txt49 = 5*(10**(len(txt)-1))-1
    num_1=''
    num_2=''
    if int(txt) >= txt49:
        num_1=txt49+1
        num_2=txt49
    else:
        num_1=int(txt)
        for j in txt:
            num_2+=str(9-int(j))
        num_2=int(num_2)
    print(num_1*num_2)