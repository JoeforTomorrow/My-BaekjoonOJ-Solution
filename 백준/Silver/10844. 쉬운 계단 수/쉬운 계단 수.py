n = int(input())

lst = [0,1,1,1,1,1,1,1,1,1]

for i in range(n-1):
    lst = [
        lst[1],
        lst[0]+lst[2],
        lst[1]+lst[3],
        lst[2]+lst[4],
        lst[3]+lst[5],
        lst[4]+lst[6],
        lst[5]+lst[7],
        lst[6]+lst[8],
        lst[7]+lst[9],
        lst[-2]
        ]

print(sum(lst)%1000000000)