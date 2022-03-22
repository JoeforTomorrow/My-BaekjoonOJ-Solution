while True:
    M=int(input())
    if M == 0:
        break
    N=2*M
    M+=1
    set1 = set(range(2, N+1)) - set(range(M))
    for i in range(2, int(N**0.5)+1):
        set1 -= set(range(2*i, N+1, i))
    lst1 = list(set1)
    lst1.sort()
    print(len(lst1))