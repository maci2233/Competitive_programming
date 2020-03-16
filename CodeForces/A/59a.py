word = input()
low = 0
high = 0
for e in word:
    if e == e.lower():
        low+=1
    else:
        high+=1
if high > low:
    print(word.upper())
else:
    print(word.lower())
