def check_log(num):
    i = 0
    while True:
        aux = 2**i
        if aux == num:
            return [True, 0]
        if aux > num:
            return [False, num-2**(i-1)]
        i+=1


def main():
    total = 0
    num = int(input())
    while True:
        total+=1
        aux = check_log(num)
        if aux[0]:
            break
        else:
            num = aux[1]
    print(str(total))

main()
