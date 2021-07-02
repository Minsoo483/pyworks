# 1번
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        return self.value


class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val
        return self.value


class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value >= 100:
            self.value = 100
        return self.value


c = Calculator()
print(c.add(10))
print(c.value)

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

cal = MaxLimitCalculator()
cal.add(50)
cal.add(51)
print(cal.value)

#4번
li = [1, -2, 3, -5, 8, -3]
print(list(filter(lambda x: x >= 0, li)))

# 완벽한 함수로 변환x


def a(x):
    if x >= 0:
        return x


b = []
for x in li:
    if a(x) != None:
        b.append(x)
print(b)


# filter -> lambda를 함수로 변환
def positive(a):
    a2=[]
    for i in a:
        if i >= 0:
            a2.append(i)
    return a2


li = [1, -2, 3, -5, 8, -3]
li2 = positive(li)
print(li2)

# 6번


def times(a):
    a2 = []
    for i in a:
        a2.append(i * 3)
    return a2


li = [1, 2, 3, 4]
print(times(li))
print(list(map(lambda x: x*3, li)))

