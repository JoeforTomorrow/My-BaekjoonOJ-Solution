import re

txt = []
while True:
    txt.extend(input().split())
    if txt[-1] == 'E-N-D': 
        break
txt = [re.sub('[^a-z-]','',i.lower()) for i in txt ]
txt.sort(key = lambda i:len(i),reverse = True)
print(txt[0].lower())