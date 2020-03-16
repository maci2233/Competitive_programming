n = int(input())
flowers = [int(i) for i in input().split()]
flowers.sort()
max = flowers[n-1] - flowers[0]
res = "" + str(max) + " "
low = 1
high = 1
i = 1
j = n-2
if max > 0:
    while flowers[i] == flowers[0]:
        low+=1
        i+=1
        if i == n:
            break
    while flowers[j] == flowers[n-1]:
        high+=1
        j-=1
        if j == -1:
            break
    res+=str(low*high)
else:
    aux = n-1
    acum = 0
    while aux > 0:
        acum+=aux
        aux-=1
    res+=str(acum)
print(res)
