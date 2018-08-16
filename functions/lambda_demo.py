def task(op, n1, n2):
    return op(n1, n2)

def mul(a, b):
    return a * b


add = lambda x,y: x + y
print(add(10,20))

print(task(add, 10, 20))
print(task(mul, 10, 20))


# task(10,20,30)
