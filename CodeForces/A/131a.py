def caps(word):
    long = len(word)
    if long == 1 and word[0] == word[0].lower():
        return True
    if word == word.upper():
        return True
    if word[0] == word[0].lower() and word[1::] == word[1::].upper():
        return True
    return False

word = input()
res = ""
if caps(word):
    for i in word:
        if i == i.lower():
            res+=i.upper()
        else:
            res+=i.lower()
    print(res)
else:
    print(word)
