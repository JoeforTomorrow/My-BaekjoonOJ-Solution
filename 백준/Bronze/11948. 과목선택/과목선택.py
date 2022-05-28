arr1 = []
arr2 = []
for _ in range(4):
    arr1.append(int(input()))
arr1.sort(reverse=True)
for _ in range(2):
    arr2.append(int(input()))
arr2.sort(reverse=True)
print(sum(arr1[:-1])+arr2[0])