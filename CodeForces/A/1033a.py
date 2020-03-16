def check():
    n = input()
    queen = [int(i) for i in input().split()]
    king = [int(i) for i in input().split()]
    win = [int(i) for i in input().split()]
    if king[1] > queen[1] and win[1] > queen[1] and king[0] < queen[0] and win[0] < queen[0]:
        return True
    if king[1] > queen[1] and win[1] > queen[1] and king[0] > queen[0] and win[0] > queen[0]:
        return True
    if king[1] < queen[1] and win[1] < queen[1] and king[0] < queen[0] and win[0] < queen[0]:
        return True
    if king[1] < queen[1] and win[1] < queen[1] and king[0] > queen[0] and win[0] > queen[0]:
        return True

if check():
    print("YES")
else:
    print("NO")
