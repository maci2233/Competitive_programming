def main():
    str1 = input().lower()
    str2 = input().lower()
    res = 0
    n = len(str1)
    for i in range(0, n):
        if ord(str1[i]) > ord(str2[i]):
            res = 1
            break
        elif ord(str1[i]) < ord(str2[i]):
            res = -1
            break
    print(res)

main()
