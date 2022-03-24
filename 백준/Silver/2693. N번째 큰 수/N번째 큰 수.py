for i in range(int(input())):
    lst=list(map(int,input().split()))
    lst.sort(reverse=True)
    del lst[:2]
    print(lst[0])