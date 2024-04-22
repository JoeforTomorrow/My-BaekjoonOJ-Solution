T = int(input())

for test_case in range(T):
    n = int(input())
    lst = [list(map(int,input().split())) for _ in range(n)]
    m = list(map(int,input().split()))[1:]
    
    coordinate_dict = {}
    for line in lst:
        if line[0] not in coordinate_dict:
            coordinate_dict[line[0]] = [line[1]]
        else:
            coordinate_dict[line[0]].append(line[1])
    
    res = []
    ptr = 0
    for i in sorted(coordinate_dict.keys()):
        if max(coordinate_dict[i]) > ptr:
            lst_tmp = sorted(coordinate_dict[i])
        else:
            lst_tmp = sorted(coordinate_dict[i], reverse=True)
        for j in lst_tmp:
            res.append([i,j])
        ptr = j
    
    for i in m:
        print(*res[i-1])