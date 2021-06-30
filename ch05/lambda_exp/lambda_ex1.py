# 매개변수가 1개 있는 lambda 함수(익명 함수)

def oneup2(x):
    return x + 1

# 1 증가 함수


oneup = lambda x: x + 1
print(oneup(2))
print((lambda x: x+1)(2))

# 3의 배수
times = lambda n: n * 3
print(times(2))
print((lambda n:n * 3)(2))
