#여러 개의 원 만들기
import turtle as t
t.shape("turtle")


n=50
t.speed(0)  # 1~9사이  0이 가장 빠름
t.color('yellow')
t.bgcolor('black')
for x in range(n):
    t.circle(80)
    t.lt(360/n)
    
t.mainloop()
