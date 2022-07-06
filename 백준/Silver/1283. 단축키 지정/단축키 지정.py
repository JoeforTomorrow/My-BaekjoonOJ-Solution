lst = []
n = int(input())
for i in range(n):
    txt = input().strip()
    switch = 0
    j = 0
    for head in txt.split():
        if head[0].lower() not in lst:
            lst.append(head[0].lower())
            switch = 1
            break
        j += len(head)+1
    if switch == 0:
        for i in range(len(txt)):
            if txt[i] != ' ':
                find = txt[i].lower()
                if find not in lst:
                    j = i
                    lst.append(find)
                    switch = 1
                    break
    if switch == 0:
        print(txt,end='')
    else:
        for i in range(len(txt)):
            if i == j:
                print(f'[{txt[i]}]',end='')
            else:
                print(txt[i],end='')
    print('')