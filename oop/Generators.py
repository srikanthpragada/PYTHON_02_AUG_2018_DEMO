def numbers(start, end):
    for n in range(start, end):
        yield n


for v in numbers(10,20):
    print(v)
