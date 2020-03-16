import math

def check_prime(square):
    num = square[0] + square[1]
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    max = math.floor(math.sqrt(num))
    for i in range(3, max, 2):
        if num % i == 0:
            return False
    return True


t = int(input())
for s in range(t):
    squares = [int(i) for i in input().split()]
    if squares[0]-squares[1] == 1 and check_prime(squares):
        print("YES")
    else:
        print("NO")
