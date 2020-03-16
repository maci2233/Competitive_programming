players = input()
n = len(players)-1
count = 1
flag = False
for i in range(0, n):
    if players[i] == players[i+1]:
        count = count+1
        if count==7:
            flag = True
            break
    else:
        count=1
if flag:
    print("YES")
else:
    print("NO")
