start_num = int(input())

for i in range(start_num):
    lst2 = []
    student = 0
    lst1 = input().split()
    lst1.pop(0)
    for j in lst1:
        lst2.append(int(j))
    avg = sum(lst2) / len(lst2)
    for k in lst2:
        if k > avg:
            student += 1
  
    print(f"{student*100/len(lst2):.3f}%")

