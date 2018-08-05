# Factorial

num = int(input("Enter a number :"))

fact = 1
for i in range(2, num + 1):
    fact *= i

print("Factorial of %d is %d" % (num, fact))
