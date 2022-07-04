lst = sorted([list(input().split()) for _ in range(int(input()))],
      key=lambda x:(int(x[-1]),int(x[-2]),int(x[-3])))
print(lst[-1][0],lst[0][0],sep='\n')