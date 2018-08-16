def iseven(n):
    return n % 2 == 0


nums = [10, 11, 35, 40, 66];
enums = filter(iseven, nums)

onums = filter(lambda n: n % 2 == 1, nums)
for n in onums:
    print(n)

names = ["Bill", "Joe", "Stephens", "Mike"]

for n in filter(lambda v: len(v) > 3, names):
    print(n)

