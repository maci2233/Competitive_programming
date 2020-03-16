def has_change():
    input()
    b25 = 0
    b50 = 0
    for e in map(int, input().split()):
        if e == 25:
            b25 += 1
            continue
        if e == 50:
            if b25 >= 1:
                b50 += 1
                b25 -= 1
                continue
            else:
                return False
        if b50 >= 1:
            b50 -= 1
            if b25 >= 1:
                b25 -= 1
                continue
            else:
                return False
        elif b25 >= 3:
            b25 -= 3
            continue
        else:
            return False
    return True

if has_change():
    print("YES")
else:
    print("NO")
