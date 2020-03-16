pieces = {'q': 9, 'r': 5, 'b': 3, 'n': 3, 'p': 1}
white = 0
black = 0
for _ in range(8):
    row = input()
    for e in row:
        if e == '.' or e.lower() == 'k':
            continue
        if e == e.lower():
            black+=pieces[e]
        else:
            white+=pieces[e.lower()]
if white > black:
    print("White")
elif black > white:
    print("Black")
else:
    print("Draw")
