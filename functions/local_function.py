gv = 100  # Global variable (Module level)


def f1():
    v1 = 10
    global  gv
    gv =  1

    def f2():  # Local function
        v2 = 20
        nonlocal v1
        v1 = v1 + 1
        print(v2, v1, gv, True)

    f2()  # call function
    print(v1)


f1()
