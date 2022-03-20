N, X = map(int,input().split())
lst = []

while True:
    if len(lst) == N:
        break
    else:
        lst = input().split()

res = ''
for i in lst:
    if int(i) < int(X):
        res += str(i)+" "
print(res.strip())