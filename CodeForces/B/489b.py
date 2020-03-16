b = int(input())
boys = [int(i) for i in input().split()]
g = int(input())
girls = [[int(i), False] for i in input().split()]
boys.sort()
girls.sort()
res = 0
for i in range(b):
    for j in range(g):
        if abs(boys[i]-girls[j][0]) <= 1:
            if girls[j][1] == False:
                res+=1
                girls[j][1] = True
                break
        else:
            continue
print(str(res))
