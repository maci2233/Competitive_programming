def check_word():
    word = input()
    for w in word:
        if w == 'H' or w == 'Q' or w == '9':
            return True
    return False

if check_word():
    print("YES")
else:
    print("NO")
