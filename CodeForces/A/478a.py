def coins():
    coins = [int(i) for i in input().split()]
    su = sum(coins)
    if su == 0:
        return '-1'
    div,mod = divmod(su,5)
    if mod == 0:
        return str(int(div))
    else:
        return '-1'

print(coins())
