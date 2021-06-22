#abs() 직접 정의해보자
import math

def abs_sign(x):
    if x < 0 :
        return x * (-1)
    else:
        return x

n1 = abs_sign(-8)
print(n1)


def abs_sign2(x):
    if x < 0 :
        return math.sqrt(x * x)
    else:
        return x
    
n2 = int(abs_sign2(-7))
print(n2)


