class A:
    def print(self):
        print("print() in A")


class B(A):
    def print(self):
        print("print() in B")


class C(B,A):
    def print(self):
        print("print() in C")


print(C.__mro__)
