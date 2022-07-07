words = input()
n = len(words)
j = -1
lst = ['<','>',' ']
arr = []
for i in range(n):
    if words[i] not in lst:
        arr.append(words[i])
    elif len(arr) != 0 and arr[0] != '<':
        if words[i] == ' ':
            for j in arr[-1::-1]:
                print(j, end='')
            arr = []
            print(' ',end='')
        else:
            for j in arr[-1::-1]:
                print(j, end='')
            arr = []
            print('',end='')
    if words[i] == "<":
        lst = ['>']
        arr.append(words[i])
    elif words[i] == ">":
        for j in arr:
            print(j,end='')
        arr = []
        print('>',end='')
        lst = ['<','>',' ']
            
            
if len(arr) != 0:
    for j in arr[-1::-1]:
        print(j, end='')