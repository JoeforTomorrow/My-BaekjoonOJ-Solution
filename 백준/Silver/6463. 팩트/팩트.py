import math
while 1:
    try:
        n = int(input())
        j = (5 - len(str(n))) * " "
        facto = str(math.factorial(n))
        k = len(facto)-1
        while 1:
            if facto[k] != "0":
                print(j + str(n) + " -> " +facto[k])
                break
            else:
                k -= 1
    except:
        break