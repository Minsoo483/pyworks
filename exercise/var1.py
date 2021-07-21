# 가변 매개변수 - (*) 튜플 자료구조
def animal(*agrs):
    print(agrs)


def avg(*args):
    sum = 0
    for i in args:
        sum += i
    return sum / len(args)


animal('cow')
animal('cow', 'pig')

# 평균 구하기
print(avg(1, 2, 3))
print(avg(1, 2, 3, 4))
