N = input()
N_2 = N[:]
res = 0
while True:
    if int(N) < 10:
        N = 2*str(int(N))
        N = str(N)
        res += 1
    else:
        N = N[-1] + str(int(N[-1])+int(N[-2]))[-1]
        res += 1
    if int(N) == int(N_2):
        break

print(res)