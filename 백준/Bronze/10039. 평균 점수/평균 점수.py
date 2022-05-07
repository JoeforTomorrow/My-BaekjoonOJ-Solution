lst = []
for i in range(5):
    a=int(input())
    if a < 40:
        lst.append(40)
    else:
        lst.append(a)
print(int(sum(lst)/5))