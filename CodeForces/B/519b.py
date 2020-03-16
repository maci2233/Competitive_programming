def create_dict(errs):
    dict = {}
    for e in errs:
        if e in dict:
            dict[e]+=1
        else:
            dict[e] = 1
    return dict


def main():
    n = int(input())
    err1 = create_dict([int(i) for i in input().split()])
    err2 = create_dict([int(i) for i in input().split()])
    err3 = create_dict([int(i) for i in input().split()])
    for e in err1:
        if e in err2:
            if err1[e] != err2[e]:
                print(str(e))
                break
        else:
            print(str(e))
            break
    for e in err2:
        if e in err3:
            if err2[e] != err3[e]:
                print(str(e))
                break
        else:
            print(str(e))
            break


main()
