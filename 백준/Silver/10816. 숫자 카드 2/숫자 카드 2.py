from sys import stdin
input = stdin.readline

def binary_search(array,target,start,end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if array[mid] == target:
        return array[start:end+1].count(target)
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)

int(input())
lst1 = sorted(list(map(int,input().split())))
int(input())
lst2 = list(map(int,input().split()))
res = {}
end = len(lst1)-1

for i in lst1:
    if i not in res:
        res[i] = binary_search(lst1,i,0,end)

res = [res[i] if (i in res) else 0 for i in lst2]

for i in res:
    print(i, end=' ')