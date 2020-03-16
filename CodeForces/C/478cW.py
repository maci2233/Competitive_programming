ballons = [int(i) for i in input().split()]
ballons.sort()
count = 0
a = ballons[0] + ballons[1]
b = ballons[2]
while a+b >= 3:
    if a >= b:
        if a >= 200000 and b >= 100000:
            a-=200000
            b-=100000
            count+=100000
        else:
            a-=2
            b-=1
            count+=1
    else:
        if b >= 200000 and a >= 100000:
            a-=100000
            b-=200000
            count+=100000
        else:
            a-=1
            b-=2
            count+=1
    if a == 0 or b == 0:
        break
print(str(count))
