lst = []

for i in range(int(input())):
    a,b = map(str,input().split())
    lst.append([int(a),b,i])
lst.sort(key=lambda x : (x[0],x[2]))

for i in lst:
    print(f"{i[0]} {i[1]}")