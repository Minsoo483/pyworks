# Person 클래서 생성과 사용
class Person:
    def __init__(self):  # 초기자(생성자 함수)
        self.name = 'hyunwoong'
        self.age = 26

    def getname(self):  # 멤버변수에 직접 접근하지 않도록 get()을 사용
        return self.name

    def getage(self):
        return self.age


p = Person()  # 객체 변수 - 인스턴스 -> 힙 메모리에 적재

print(p.name)
print(p.getage())