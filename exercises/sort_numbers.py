
nums = []
count = 0
while True:
    try:
        num = int( input("Enter a number :"))
        nums.append(num)
        count += 1
        if count == 5:
            break
    except ValueError:
        print("Invalid Number! Please try again!")

for n in sorted(nums):
    print(n)


