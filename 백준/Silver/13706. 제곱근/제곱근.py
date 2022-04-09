n = int(input())
low = 1
high = n
while 1:
    avg=(low + high) // 2
    if avg ** 2 == n:
        print(avg)
        break
    elif avg ** 2 > n:
        high = avg - 1
    elif avg ** 2 < n:
        low = avg + 1