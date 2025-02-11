import turtle
t=turtle.Turtle()
turtle.title("Luka Turtle Python Graphics")
class lukaturtle:
    def __init__(self):
        pass
    def triangle(self, a, b, c):
        t.fd(a)
        t.lt(120)
        t.fd(b)
        t.lt(120)
        t.fd(c)
        t.lt(120)
        turtle.done()
    def rectangle(self, a, b):
        for _ in range(2):
            t.fd(a)
            t.lt(90)
            t.fd(b)
            t.lt(90)
        turtle.done()
    def shape(self, a, b):
        if a >= 3:
            for _ in range(a):
                t.fd(b)
                t.lt(360 // a)
            turtle.done()
        else:
            print("The number of sides must be greater then 2.")
    def title(self, usertitle):
        turtle.title(usertitle)
    def test(self):
        pass
    def stickman(self, a):
        b = a * 4
        t.circle(a)
        t.lt(270)
        t.fd(b)
        t.lt(180)
        t.fd(b//2)
        t.rt(45)
        t.fd(a)
        t.lt(180)
        t.fd(a)
        t.rt(90)
        t.fd(a)
        t.lt(180)
        t.fd(a)
        t.rt(45)
        t.fd(a*2)
        t.lt(45)
        t.fd(a)
        t.lt(180)
        t.fd(a)
        t.lt(90)
        t.fd(a)
        turtle.done()