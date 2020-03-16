def magic(num):
    test = int(num)
    lucky = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477]
    for i in num:
        if i != '4' and i != '7':
            for x in lucky:
                if test % x == 0:
                    return True
            return False
    return True

num = input()
if magic(num):
    print("YES")
else:
    print("NO")
