word = input()
unique = ""
sum = 0
for i in word:
    found = False
    for c in unique:
        if i == c:
            found = True
            break
    if not found:
        sum+=1
        unique+=i
if sum % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
