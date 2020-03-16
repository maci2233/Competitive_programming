def pro():
    a,b = [int(i) for i in input().split()]
    if a > b:
        if a - 1 == b:
            return '01' * b + '0'
        else:
            return '-1'
    res = ''
    while b - 1 > a and a > 0:
        res += '110'
        a -= 1
        b -= 2
        if a == 0 and b >= 3:
            return '-1'
    while a > 0 or b > 0:
        if b > 0:
            res += '1'
            b -= 1
        if a > 0:
            res += '0'
            a -= 1
    return res

print(pro())
