from ch07.myclass.calcultor import Calculator
# Calculator를 확장한 MoreCalculator 클래스 만들기


class MoreCalculator(Calculator):
    def pow(self):
        return self.x ** self.y

    def div(self):
        if self.y == 0:
            return 0
        else:
            return self.x / self.y


cal = MoreCalculator(2, 0)
print(cal.pow())
print(cal.add())
print(cal.div())