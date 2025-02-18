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
                t.lt(360 / a)
            turtle.done()
        else:
            print("The number of sides must be greater then 2.")
        turtle.done()
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
    def fd(self, a):
        t.fd(a)
        turtle.done()
    def bk(self, a):
        t.bk(a)
        turtle.done()
    def lt(self, a):
        t.lt(a)
        turtle.done()
    def rt(self, a):
        t.rt(a)
        turtle.done()
    def st(self):
        t.st()
    def ht(self):
        t.ht()
    def pu(self):
        t.pu()
    def pd(self):
        t.pd()
    def pencolor(self, a):
        t.pencolor(a)
    def pensize(self, a):
        t.pensize(a)
    def begin_fill(self):
        t.begin_fill()
    def fillcolor(self, a):
        t.fillcolor(a)
    def end_fill(self):
        t.end_fill()
    def heart(self, a):
        t.lt(140)
        t.fd(a)
        t.circle(-a * 0.4, 200)
        t.lt(120)
        t.circle(-a * 0.4, 200)
        t.fd(a)
        turtle.done()
