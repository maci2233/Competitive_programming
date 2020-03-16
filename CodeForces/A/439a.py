def max_songs(n,k,songs):
    rest = 10*(n-1)
    total = rest + sum(songs)
    if total > k:
        return -1
    else:
        return (k-total+rest) // 5

def main():
    n,k = [int(i) for i in input().split()]
    s = [int(i) for i in input().split()]
    print(str(max_songs(n,k,s)))

main()
