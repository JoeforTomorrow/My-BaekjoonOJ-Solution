dic = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0}
lst1 = 0
lst2 = 0
while True:
    try:
        score,grade=input().split()[1:]
        if grade != "P":
            lst1 += float(score)*dic[grade]
            lst2 += float(score)
    except:
        break
print(f'{lst1/lst2:.6f}')