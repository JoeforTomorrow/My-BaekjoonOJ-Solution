a,b=([int(input()) for i in range(9)],0);print(max(a))
for i in a:
    b+=1
    if i == max(a):
        print(b)
        break