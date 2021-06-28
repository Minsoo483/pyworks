from person import Person
# 멤버 매개변수가 있는 상속

class Employee(Person):
    def __init__(self, name, age, empid):
        super().__init__(name, age)  # 부모의 name, age를 받아온다. // 부모 멤버는 super()를 사용
        self.empid = empid

    def getname(self):
        return self.name

    def getage(self):
        return self.age

    def getempid(self):
        return self.empid



e1 = Employee("북한산", 20, 201)
print("이름 : ", e1.getname())
print("나이 : ", e1.getage())
print("사원번호 : ", e1.getempid())

e2 = Employee("금강", 30, 202)
print("이름 : ", e2.getname())
print("나이 : ", e2.getage())
print("사원번호 : ", e2.getempid())
