n = int(input())
names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
steps = 1
aux = steps
i = 0
while n > 1:
    if n <= steps:
        break
    n-=steps
    i+=1
    if i == 5:
        steps*=2
        i=0
print(names[i])
