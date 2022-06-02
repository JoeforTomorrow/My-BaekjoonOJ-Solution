while True:
    try:
        n = int(input())
        m = len(str(n))
        while True:
            num = int('1' * m)
            if num%n != 0:
                m += 1
            else:
                break
        print(m)
    except:
        break