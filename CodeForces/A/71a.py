test = int(input())
for i in range(0,test):
    word = input()
    n = len(word)
    if n <= 10:
        print(word)
    else:
        print(word[0] + str(n-2) + word[n-1])
