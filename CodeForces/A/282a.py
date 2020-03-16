n = int(input())
x = 0
for i in range(0, n):
    oper = input()
    if oper.find('+') != -1:
        x = x+1
    else:
        x = x-1
print(x)
