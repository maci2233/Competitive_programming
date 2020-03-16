word = input()
aux = word
n = len(word)
res = 1
while True:
    word2 = aux[n-1] + aux[0:n-1]
    if word2 != word:
        res+=1
        aux=word2
    else:
        break
print(str(res))
