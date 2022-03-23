while True:
    a,b,c = map(int,input().split())
    lst1 = [a,b,c]
    lst2 = lst1[:]
    if lst1[0] == 0:
        break
    lst2.remove(max(lst1))
    if lst2[0]**2 + lst2[1]**2 == max(lst1)**2:
        print("right")
    else:
        print("wrong")