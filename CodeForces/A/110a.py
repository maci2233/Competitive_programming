def is_lucky():
    number = [int(i) for i in input()]
    n = 0
    for i in number:
        if i == 4 or i == 7:
            n+=1
    magic_numbers = [i for i in str(n)]
    for i in magic_numbers:
        if i != '4' and i != '7':
            return False
    return True


if is_lucky():
    print("YES")
else:
    print("NO")
