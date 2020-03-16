import math

def is_composite(num):
    if num <= 2:
        return False
    if num % 2 == 0:
        return True
    max = math.ceil(math.sqrt(num))
    for n in range(3, max+1, 2):
        if num % n == 0:
            return True
    return False


def main():
    n = int(input())
    a = n//2
    b = math.ceil(n/2)
    while True:
        if is_composite(a) and is_composite(b):
            print(str(a) + ' ' + str(b))
            break
        else:
            a-=1
            b+=1


main()
