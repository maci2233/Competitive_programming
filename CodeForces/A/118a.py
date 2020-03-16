def main():
    string = input().lower()
    vowels = "aoyeui"
    res = ''
    for i in string:
        if vowels.find(i) != -1:
            continue
        else:
            res = res + '.' + i
    print(res)

main()
