n = int(input())
word = input()
i = 0
aux = 2
res = ''
while i < n:
    res += word[i]
    i += aux
    aux += 1
print(res)
