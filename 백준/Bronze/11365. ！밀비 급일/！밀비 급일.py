sentences = []
while True:
    sentence = input()
    if sentence != 'END':
        sentences.append(sentence[::-1])
    else: break
for sentence in sentences:
    print(sentence)