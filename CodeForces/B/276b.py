word = input()
lets = [0] * 26
for c in word:
    lets[ord(c) - 97] += 1
c = 0
for e in lets:
    if e % 2 == 1:
        c += 1
if c == 0 or c % 2 == 1:
    print('First')
else:
    print('Second')
