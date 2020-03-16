move = input()
msg = input()
keyboard = 'qwertyuiopasdfghjkl;zxcvbnm,./'
res = ""
for e in msg:
    if move == 'L':
        res+=keyboard[keyboard.find(e)+1]
    else:
        res+=keyboard[keyboard.find(e)-1]
print(res)
