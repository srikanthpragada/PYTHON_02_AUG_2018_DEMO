import sys

a = 10
b = 0
try:
    b = int("0")
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Division by Zero")
    sys.exit(0)
else:
    print("Completed!")
finally:
    print("Done")

print("The End")