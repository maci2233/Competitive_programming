n = int(input())
if n % 2 != 0 or n <= 4:
    print('0')
else:
    half = n // 2 - 1
    quart = n // 4
    print(half - quart)
