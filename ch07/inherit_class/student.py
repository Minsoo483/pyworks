from person import Person
# Student 클래스


class Student(Person):
    def __init__(self, name, age, sid):
        super().__init__(name, age)
        self.sid = sid

    def showinfo(self):
        print(self.name, self.age, self.sid)


s1 = Student("이강", 19, 101)
s1.showinfo()
s1 = Student("찬들", 17, 102)
s1.showinfo()
