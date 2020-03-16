x1,y1,x2,y2 = [int(i) for i in input().split()]
if x1 == x2:
    dif = y2-y1
    print(str(x1+dif) + ' ' + str(y1) + ' ' + str(x2+dif) + ' ' + str(y2))
elif y1 == y2:
    dif = x2-x1
    print(str(x1) + ' ' + str(y1+dif) + ' ' + str(x2) + ' ' + str(y2+dif))
elif abs(x2-x1) == abs(y2-y1):
    print(str(x1) + ' ' + str(y2) + ' ' + str(x2) + ' ' + str(y1))
else:
    print('-1')
