n = int(input())
matches = input()
anton = matches.count('A')
mid = n/2
if anton > mid:
    print('Anton')
elif anton == mid:
    print('Friendship')
else:
    print("Danik")
