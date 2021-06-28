#학생 클래스 만들기
class Student:
    def __init__(self, sid, name):
        self.__sid = sid  # __ 정보은닉으로 멤버변수를 바로 참조 불가
        self.__name = name

    def getsid(self):  # get멤버변수 메소드를 이용해야 멤버변수 이용가능
        return self.__sid

    def getname(self):
        return self.__name


s1 = Student(1001, '김산')
print(s1.getsid(), s1.getname())
s2 = Student(1002, '이강')
print(s2.getsid(), s2.getname())



