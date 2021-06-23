#다른 곳에 도형 그리기
import turtle as t

def polygon(n):
    for x in range(n):
        t.fd(100)
        t.lt(360/n)

def polygon2(n,d):
    for x in range(n):
        t.fd(d)
        t.lt(360/n)


for x in range(3,10):
    t.speed(0)
    polygon(x)
    t.up()
    t.fd(1)
    t.down()
    

