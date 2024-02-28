import bisect

n = input()
lst = list(map(int,input().split()))

arr = [lst[0]]

for n, i in enumerate(lst):
    if arr[-1] < i:
        arr.append(i)
    else:
        idx = bisect.bisect_left(arr, i)
        arr[idx] = i

print(len(arr))