n = int(input())
for i in range(0, n):
    a = float(input())
    if 360.0 % (180.0-a) == 0:
        print("YES")
    else:
        print("NO")
    
