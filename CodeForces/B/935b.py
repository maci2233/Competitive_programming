n = int(input())
steps = input()
x = 0
y = 0
count = 0
if steps[0] == 'U':
    pos = 0
    y = 1
else:
    pos = 1
    x = 1
for i in range(1,n):
    if steps[i] == 'U':
        y+=1
        if pos == 1 and y > x:
            count+=1
            pos = 0
    else:
        x+=1
        if pos == 0 and x > y:
            count+=1
            pos = 1
print(str(count))
