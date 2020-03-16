n = int(input())
last = [8,4,2,6]
if n == 0:
    print('1')
else:
    print(str(last[n%4 - 1]))
