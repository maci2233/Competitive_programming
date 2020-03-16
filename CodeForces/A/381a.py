n = int(input())
numbers = [int(i) for i in input().split()]
sum1 = 0
sum2 = 0
turn = 0
last = n
for x in range(n):
    if numbers[0] > numbers[last-1]:
        max = numbers[0]
        numbers.remove(numbers[0])
    else:
        max = numbers[last-1]
        numbers.remove(numbers[last-1])
    last-=1
    if turn == 0:
        sum1+=max
        turn = 1
    else:
        sum2+=max
        turn = 0

print(str(sum1) + " " + str(sum2))
