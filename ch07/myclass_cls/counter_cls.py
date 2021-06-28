# 인스턴스 변수 와 클래스 변수
class Counter:
    x = 0  # 클래스 변수

    def __init__(self):

        Counter.x += 1  # self가 아니라 클래스 이름으로 접근

    def showinfo(self):
        print(self.x)


c1 = Counter()
c1.showinfo()
c2 = Counter()
c2.showinfo()
c3 = Counter()
c3.showinfo()
