nums = []

while True:
    num = int(input("Enter a number :"))
    if num == 0:
        break

    if num % 2 == 0:    # Even number at the beginning
        nums.insert(0, num)
    else:
        nums.append(num)  # Odd at the end

for n in nums:
    print(n)
