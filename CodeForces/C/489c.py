def min_num(m,s):
    unit = 1
    acum = 0
    num = 0
    for i in range(m):
        dig = 9
        if i+1 < m:
            while dig+acum >= s and dig >= 0:
                dig-=1
        else:
            while dig+acum > s and dig >= 0:
                dig-=1
        acum+=dig
        num+=dig*unit
        unit*=10
    if acum != s or (s == 0 and m > 1):
        return -1
    else:
        return num

def max_num(m,s):
    num = ''
    for i in range(m):
        low = min(9,s)
        num+=str(low)
        s-=low
    return num

def main():
    m,s = [int(i) for i in input().split()]
    min = str(min_num(m,s))
    if min == '-1':
        print('-1 -1')
    else:
        print(str(min) + ' ' + max_num(m,s))

main()
