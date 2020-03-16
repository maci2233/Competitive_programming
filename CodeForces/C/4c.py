n = int(input())
names = {}
for i in range(n):
    word = input()
    if word not in names:
        names[word] = 1
        print("OK")
    else:
        print(word + str(names[word]))
        names[word]+=1
