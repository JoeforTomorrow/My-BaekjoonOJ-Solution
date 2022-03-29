import sys
input = sys.stdin.readline
for i in range(int(input())):
    input()
    lst_1 = list(map(str,input().split()))
    lst_2 = list(map(str,input().split()))
    lst_1.sort(key = lambda x :(x[0], x[1]))
    lst_2.sort(key = lambda x :(x[0], x[1]))
    if lst_1 != lst_2:
        print("CHEATER")
    else:
        print("NOT CHEATER")