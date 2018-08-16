def total(*nums, msg='Total'):
    print(msg, sum(nums))


def wish(msg,*names):
    for n in names:
        print(msg, n)


total(10, 20, msg='Total Marks')
total(1, 2, 3)
wish("Hello", "Andy", "Bob")



