word1 = input()
word2 = input()
n = len(word1)
res = ""
for i in range(n):
    if word1[i] == word2[i]:
        res+="0"
    else:
        res+="1"
print(res)
