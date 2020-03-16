def optimal(num):
    int_num = int(num)
    if int_num >= 0:
        return num
    elif int_num >= -10:
        return 0
    else:
        if num[-2] > num[-1]:
            res = num[0:-2] + num[-1]
        else:
            res = num[0:-1]
    if res == '-0':
        return 0
    return res

def main():
    n = input()
    print(optimal(n))

main()
