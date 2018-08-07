# Display average of positive numbers
total = count = 0
while True:
    num = int(input("Enter a number :"))
    if num == 0:
        break

    if num < 0:
        continue

    total += num
    count += 1

print("Average = ", total / count)
