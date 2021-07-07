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

# 7번


def find_max(li):
    max = li[0]
    for i in range(1, len(li)):
        if li[i] >= max:
            max = li[i]
    return max


def find_min(li):
    min = li[0]
    for i in li:
        if i <= min:
            min = i
    return min


d1 = [-8, 2, 7, 5, -3, 5, 0, 1]
max2 = find_max(d1)
min2 = find_min(d1)
print(max2)
print(min2)
print(max2 + min2)
'''
max = max(d1)
min = min(d1)

print(max)
print(min)
print(max + min)'''

# 12번
import time
import datetime

now1 = time.strftime("%Y/%m/%d %H:%M:%S")
print(now1)

now2 = datetime.datetime.now()
print(now2.strftime("%Y/%m/%d %H:%M:%S"))
