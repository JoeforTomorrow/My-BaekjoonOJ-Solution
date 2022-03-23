a = int(input())
lst = []
for i in range(a):
    lst += map(int,(input().split()))
    lst.sort(reverse=True)
    while len(lst) != a:
        lst.pop()
print(lst.pop())