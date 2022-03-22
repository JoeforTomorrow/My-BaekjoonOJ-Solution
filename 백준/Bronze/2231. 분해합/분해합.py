num = int(input())
res = 0
a = int(num/2)
B = False
for i in range(a,num):
    for j in range(len(str(i))):
        res += int(str(i)[int(j)])
    res += i
    if res == num:
        print(i)
        B = True
        break
    res = 0
if B == False: print(0)