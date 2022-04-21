txt = input()
lst = [ txt[i] for i in range(len(txt))]
num_dict = {
    2 : "ABC",
    3 : "DEF",
    4 : "GHI",
    5 : "JKL",
    6 : "MNO",
    7 : "PQRS",
    8 : "TUV",
    9 : "WXYZ"
}
res = 0
for i in num_dict:
    for j in lst:
        if j in num_dict[i]:
            res += i + 1
print(res)
    