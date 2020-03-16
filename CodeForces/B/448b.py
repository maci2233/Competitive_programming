def lcss(s1, s2):
    n = len(s1)
    m = len(s2)



word1, word2 = input(), input()
n, m = len(word1), len(word2)
c2 = {}
for e in word2:
    if e not in c2:
        c2[e] = 1
    else:
        c2[e] += 1
for e in word2:
    if word1.count(e) < c2[e]:
        print('need tree')
        exit()
if n < m:
    print('need tree')
elif n > m:
    pass
    #CHECAR LONGEST COMMON SUBSEQUENCE
else:
    print('array')
