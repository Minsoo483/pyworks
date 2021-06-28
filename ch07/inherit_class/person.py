class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showinfo(self):
        print(self.name, self.age)


class Employee(Person):  # Person 상속
    pass


if __name__ == "__main__":
    p1 = Person("현웅", 26)
    p1.showinfo()

    e1 = Employee("아아으", 90)
    e1.showinfo()

    e2 = Employee("북한강", 35)
    e2.showinfo()

