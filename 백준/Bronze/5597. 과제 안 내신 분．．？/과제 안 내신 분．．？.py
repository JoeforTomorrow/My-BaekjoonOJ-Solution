handin_lst = []
student_set = set(list(range(1,31)))
for _ in range(0,28):
    student = int(input())
    handin_lst.append(student)
handin_set = set(handin_lst)
not_handin_lst = list(student_set.difference(handin_set))
not_handin_lst.sort()
for num in not_handin_lst:
    print(num)