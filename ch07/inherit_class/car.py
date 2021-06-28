# Car 클래스 _ Bus, Taxi가 자식 클래스 -> 오버라이딩

class Car:
    def drive(self):
        print("차가 주행합니다.")


class Taxi(Car):
    def drive(self):
        print("택시가 주행합니다.")


class Bus(Car):
    def drive(self):
        print("버스가 주행합니다.")


c = Car()
c.drive()

b = Bus()
b.drive()


