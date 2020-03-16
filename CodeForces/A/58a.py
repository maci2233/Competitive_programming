word = input()
check = "hello"
char = 0
for i in word:
    if i == check[char]:
        char+=1
        if char == 5:
            break
if char == 5:
    print("YES")
else:
    print("NO")
