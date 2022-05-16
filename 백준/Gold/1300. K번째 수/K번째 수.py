a,b=int(input()),int(input())
end=b
def binary_search(start,end,a,b):
    while start <= end:
        mid = (start+end)//2
        n = 0
        for i in range(1,a+1):
            n += min(mid//i, a)
        if n >= b:
            res = mid
            end = mid - 1
        else:
            start = mid + 1
    print(res)
binary_search(1,end,a,b)