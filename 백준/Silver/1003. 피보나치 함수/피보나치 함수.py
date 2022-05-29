import sys
input = sys.stdin.readline

for _ in range(int(input())):
    arr0 = [1,0]
    arr1 = [0,1]
    n = int(input())
    if n > 1:
        for i in range(n-1):
            arr0.append(arr1[-1])
            arr1.append(arr0[-2]+arr1[-1])
    print(arr0[n], arr1[n])