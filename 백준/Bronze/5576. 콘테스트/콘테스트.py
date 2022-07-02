arr1 = sorted([int(input()) for _ in range(10)],reverse=True)
arr2 = sorted([int(input()) for _ in range(10)],reverse=True)
print(sum(arr1[:3]),sum(arr2[:3]))