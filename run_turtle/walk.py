

import random as r
import turtle as t

t.shape("turtle")
t.speed(0)
t.bgcolor('pink')


for x in range(300):
    angle = r.randint(1, 360)
    t.setheading(angle)
    t.fd(20)
    
