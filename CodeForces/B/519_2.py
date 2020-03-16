def create_dict(nums):
    d = {}
    for num in nums:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    return d

input()
d1 = create_dict([int(i) for i in input().split()])
d2 = create_dict([int(i) for i in input().split()])
d3 = create_dict([int(i) for i in input().split()])
for key in d1.keys():
    if key not in d2 or d1[key] != d2[key]:
        print(key)
        break
for key in d2.keys():
    if key not in d3 or d2[key] != d3[key]:
        print(key)
        break
