import sys
input = sys.stdin.readline

def binary_search(array,target,start,end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

int(input())
lst1 = sorted(list(map(int,input().split())))
int(input())
lst2 = list(map(int,input().split()))

for i in lst2:
    print(1) if binary_search(lst1,i,0,len(lst1)-1) != None else print(0)