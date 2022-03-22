a = input().split()
n = 0
for i in range(0,5):
    n += int(a[i])**2
print(n%10)