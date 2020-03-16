def main():
    str = input().split()
    n = int(str[0])
    k= int(str[1])
    scores = input().split()
    scores[k-1] = int(scores[k-1])
    total = 0
    for i in range(0,n):
        scores[i] = int(scores[i])
        if scores[i] >= scores[k-1] and scores[i] > 0:
            total = total+1
    print(total)

main()
