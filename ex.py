A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for i in A:
    total += i
    average = total / len(A)

print(average)

numbers = [1, 2, 3, 4, 5]
result = []
for i in numbers:
    if i % 2 == 1:
        result.append(i*2)

print(result)


class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val


class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value >= 100:
            self.value = 100


cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)


cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)

