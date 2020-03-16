a,b = [int(i) for i in input().split()]
count = 0
while a <= b:
    count+=1
    a*=3
    b*=2
print(str(count))
