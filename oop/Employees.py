class Employee(object):
    def __init__(self, no, name):
        self.empno = no
        self.name = name

    def print(self):
        print(self.empno)
        print(self.name)

    def __str__(self):
        return str(self.empno) + " - " + self.name


class SalariedEmployee(Employee):
    def __init__(self, no, name, salary):
        super().__init__(no, name)
        self.salary = salary

    def print(self):
        Employee.print(self)
        print(self.salary)

    def get_salary(self):
        return self.salary


class Consultant(Employee):
    def __init__(self, no, name, hours, rate):
        super().__init__(no, name)
        self.hours = hours
        self.rate = rate

    def print(self):
        Employee.print(self)
        print(self.hours)
        print(self.rate)

    def get_salary(self):
        return self.hours * self.rate


e = Employee(1, "Mr. Bill")
print(e.__str__())
e.print()

se = SalariedEmployee(2, "Mr.Scott", 100000)
se.print()

c = Consultant(3, "Mr. Tom", 10, 1000)
c.print()
