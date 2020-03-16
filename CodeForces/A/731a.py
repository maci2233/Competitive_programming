word = input()
curr = 0
res = 0
for e in word:
    val = ord(e)-97
    if curr < val:
        res+=min(val-curr, curr+26-val)
    elif curr > val:
        res+=min(curr-val, 26-curr+val)
    else:
        continue
    curr = val
print(str(res))
