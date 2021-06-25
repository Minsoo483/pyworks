import turtle as t

t.shape("turtle")

#사각형
n = 4
for i in range(n):
    t.fd(100)
    t.rt(360/n)

#삼각형
n = 3
t.color('blue')
t.pensize(2)
for i in range(n):
    t.rt(360/n)
    t.fd(100)


#원
t.color('red')
t.pensize(3)
t.circle(50)

#n각형 그리기
n =  8
t.color('green')
t.pensize(2)
for i in range(n):
    t.rt(360/n)
    t.fd(100)

t.mainloop()
