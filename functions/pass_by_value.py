
def swap(n1,n2):
    n1, n2 = n2, n1
    print('Inside swap()')
    print(id(n1), n1)
    print(id(n2), n2)


a = 10
print(id(a))
b = 20
print(id(b))
c = a
print(id(c))

swap(a,b)
print(a,b)


