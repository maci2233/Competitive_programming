n = int(input())
num = input()
eq = ['','','2','3','322','5','53','7','7222','7332']
res = []
for e in map(int, num):
    res.append(eq[e])
a = ''.join(str(i) for i in res)
a = sorted(a, reverse = True)
print(''.join(i for i in a))
