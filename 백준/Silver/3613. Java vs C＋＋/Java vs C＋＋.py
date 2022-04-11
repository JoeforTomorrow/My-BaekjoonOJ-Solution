def print_txt(txt):
    word = ""
    for i in txt:
        word += i
    print(word)

def cToJava(txt):
    for i in range(len(txt)):
        if txt[i] == "_":
            txt[i] = ""
            txt[i+1] = txt[i+1].upper()
    print_txt(txt)

def java_to_c(txt):
    for i in range(len(txt)):
        if txt[i] == txt[i].upper():
            txt[i] = "_" + txt[i].lower()
    print_txt(txt)


txt = list(map(str,input()))

switch = 1
while True:
    if "_" in txt:
        if txt[0] == "_":
            switch = 0
        elif txt[-1] == "_":
            switch = 0
        for i in range(len(txt)):
            if txt[i] == "_":
                if txt[i-1] == "_":
                    switch = 0
                    break
        for i in txt:
            if i.isupper() == True:
                switch = 0
                break
        if switch == 1:
            cToJava(txt)
    else:
        if txt[0].isupper() == True:
            switch = 0
        else:
            java_to_c(txt)
    break


if switch == 0:
    print("Error!")