import sys
input = sys.stdin.readline
x = set([str(i) for i in range(1,21)])
st = set()
for i in range(int(input())):
    txt = input().rstrip()
    if txt[:2] == "ad":
        st = st.union(set([txt[4:]]))
    elif txt[:1] == "c":
        if txt[6:] not in st:
            print(0)
        else:
            print(1)
    elif txt[:1] == "t":
        if txt[7:] not in st:
            st = st.union(set([txt[7:]]))
        else:
            st = st.difference(set([txt[7:]]))
    elif txt[:1] == "r":
        st = st.difference(set([txt[7:]]))
    elif txt == "all":
        st = x.copy()
    elif txt == "empty":
        st = set()