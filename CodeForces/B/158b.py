n = int(input())
groups = [int(i) for i in input().split()]
groups.sort(reverse=True)
j = n-1
res = 0
i = 0
while(i < n):
    if i > j:
        break
    if groups[i] == 4:
        res+=1
    if groups[i] == 3:
        if groups[j] == 1:
            j-=1
        res+=1
    if groups[i] == 2:
        if i+1 < n:
            if groups[i+1] == 2:
                i+=1
            else:
                if groups[j] == 1:
                    j-=1
                    if groups[j] == 1:
                        j-=1
        res+=1
    if groups[i] == 1:
        aux = 0
        while(i+1 <= n and aux < 4 and i <= j):
            i+=1
            aux+=1
        i-=1
        res+=1
    i+=1
print(str(res))
