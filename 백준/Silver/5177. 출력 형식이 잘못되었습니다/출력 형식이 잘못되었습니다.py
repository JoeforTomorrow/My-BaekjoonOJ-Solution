n=int(input())
for i in range(n):
    a=input()
    b=input()
    a=a.replace("(","").replace(")","").replace("[","").replace("]","").replace("{","").replace("}","").replace(".","").replace(",","").replace(";","").replace(":","").lower().split()
    b=b.replace("(","").replace(")","").replace("[","").replace("]","").replace("{","").replace("}","").replace(".","").replace(",","").replace(";","").replace(":","").lower().split()
    if a==b:
        print(f'Data Set {i+1}: equal')
    else:
        print(f'Data Set {i+1}: not equal')
    if i != n:
        print('')