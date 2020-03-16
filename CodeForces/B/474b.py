input()
pos = []
aux = 1
for e in input().split():
    pos+=[aux]*int(e)
    aux+=1
input()
for e in input().split():
    print(str(pos[int(e)-1]))
