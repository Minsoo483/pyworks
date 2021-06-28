import turtle as t
import random


def turn_right():
    t.setheading(0)


def turn_up():
    t.setheading(90)


def turn_left():
    t.setheading(180)


def turn_down():
    t.setheading(270)


def start():
    global playing
    if playing == 0:
        playing = 1
        t.clear()
        play()


def message(m1, m2):
    t.clear()
    t.goto(0, 100)
    t.write(m1, 0, "center", ("", 20))
    t.goto(0, -100)
    t.write(m2, 0, "center", ("", 15))
    t.home()  # t를 (0, 0) 으로 보냄


def play():
    global score
    global playing

    t.fd(10)

    #적 거북이 속도
    if random.randint(1, 5) == 3:
        ang = te.towards(t.pos())
        te.setheading(ang)
    speed = score + 5
    if speed > 15:
        speed = 15
    te.fd(speed)

    #먹이
    if t.distance(tf) < 12:
        score += 1
        t.write(score)
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        tf.goto(x, y)

    # 게임종료
    if t.distance(te) < 12:
        text = "Score : " + str(score)
        message("Game Over", text)
        playing = 0
        score = 0
        te.goto(0, 200)
        tf.goto(0, -200)

    if playing:
        t.ontimer(play, 100)

# 메인 영역
score = 0
playing = False # 게임 스위치

t.setup(500, 500)
t.title("달려라 거북이")
t.bgcolor('orange')
t.shape('turtle')
t.speed(0)
t.up()
t.color('white') # 주인공 거북이

# 적 거북이
te = t.Turtle() # Turtle() 클래스에서 te 인스터스 생성
te.shape('turtle')
te.color('red')
te.speed(0)
te.up()
te.goto(0, 200)

# 먹이
tf = t.Turtle()
tf.shape("circle")
tf.color('green')
tf.speed(0)
tf.up()
tf.goto(0, -200)

t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(start, "space")
t.listen()
message("Turtle Run", "[Space]")

t.mainloop()
