def buttons(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    i = 2
    tot = n
    while i < n:
        tot+=((n-i)*i)+1
        i+=1
    return tot+1


def main():
    n = int(input())
    print(str(buttons(n)))


main()
