txt = input()
bomb = input()

bomb_char = bomb[-1]
stack = []
bomb_length = len(bomb)

for letter in txt:
    stack.append(letter)
    if letter == bomb_char and ''.join(stack[-bomb_length:]) == bomb:
        del stack[-bomb_length:]
        
res = ''.join(stack)

if res == '':
    print("FRULA")
else:
    print(res)