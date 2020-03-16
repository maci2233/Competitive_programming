test = int(input())
coins = [int(c) for c in input().split()] #LIST COMPREHENSION
total = sum(coins)/2
coins.sort(reverse=True)
acum = 0
res = 0
for i in coins:
    acum+=i
    res+=1
    if acum > total:
        break
print(res)
