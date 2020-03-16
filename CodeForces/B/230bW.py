import math

def tprime2():
    extra = int(input())
    numbers = [int(i) for i in input().split()]
    res = ""
    for i in numbers:
        num = math.sqrt(i)
        if num % 1 != 0:
            res+='NO\n'
            continue
        elif num == 1:
            res+='NO\n'
            continue
        elif num == 2:
            res+='YES\n'
            continue
        elif num % 2 == 0:
            res+='NO\n'
            continue
        else:
            max = math.ceil(math.sqrt(i))
            prime = True
            for n in range(3, max, 2):
                if num % n == 0:
                    prime = False
                    break
            if prime:
                res+='YES\n'
            else:
                res+='NO\n'
            continue
    print(res)

tprime2()
