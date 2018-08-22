class A:
    def print(self):
        print("print() in A")


class B:
    def print(self):
        print("print() in B")


class C(A):
    def print(self):
        print("print() in C")


class D(C,B):
    def print(self):
        print("print() in D")


print(D.__mro__)
