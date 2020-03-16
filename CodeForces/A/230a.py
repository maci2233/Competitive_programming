def beat_dragons(s, n, dragons):
    for i in range(n):
        if s > dragons[i][0]:
            s+=dragons[i][1]
        else:
            return False
    return True

def main():
    s,n = [int(i) for i in input().split()]
    dragons = []
    for i in range(n):
        pair = input().split()
        dragons.append((int(pair[0]), int(pair[1])))
    dragons.sort()
    print("YES") if beat_dragons(s, n, dragons) else print("NO")

main()
