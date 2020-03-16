res = ''
non_zero = False
for n in map(int, input()):
    if 9-n < n:
        if 9-n == 0:
            if non_zero:
                res += str(9-n)
            else:
                res += str(n)
                non_zero = True
        else:
            res += str(9-n)
            non_zero = True
    else:
        res += str(n)
        non_zero = True
print(res)
