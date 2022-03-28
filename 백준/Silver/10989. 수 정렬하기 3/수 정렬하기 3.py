import sys
res = [0] * 10001
for i in range(int(sys.stdin.readline())):
    res[int(sys.stdin.readline())]+=1
for i in range(10000,0,-1):
    if res[i] != 0:
        del res[i+1:]
        break
for i in range(1,len(res)):
    if res[i] !=0:
        for j in range(res[i]):
            print(i)