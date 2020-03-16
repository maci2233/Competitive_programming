#SOLUCION CON XOR
n,m,k = [int(i) for i in input().split()]
enemy = []
for _ in range(m):
    enemy.append(int(input()))
f = int(input())
res = 0
for e in enemy:
    if bin(e^f).count('1') <= k:
        res+=1
print(str(res))


#SOLUCION CON STRINGS
'''
enemy = []
for _ in range(m):
    enemy.append(bin(int(input()))[2:][::-1])
f = bin(int(input()))[2:][::-1]
le1 = len(f)
res = 0
for e in enemy:
    le2 = len(e)
    aux = 0
    for i in range(min(le1,le2)):
        if f[i] != e[i]:
            aux+=1
            if aux > k:
                break
    if aux > k:
        continue
    if le1 < le2:
        for i in range(le1, le2):
            if e[i] == '1':
                aux+=1
    elif le2 < le1:
        for i in range(le2, le1):
            if f[i] == '1':
                aux+=1
    if aux <= k:
        res+=1
print(str(res))
'''
