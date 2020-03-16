n = int(input())
level = 1
inc = 2
total = 1
aux = 1
while total <= n:
    level+=1
    aux+=inc
    total+=aux
    inc+=1
print(str(level-1))
