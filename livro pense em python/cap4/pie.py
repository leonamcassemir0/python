import turtle

leo = turtle.Turtle()


def polygon(t, n):
    angle = 360 / n
    for i in range(n):
        t.fd(100)
        t.lt(angle)   
    triangle(t, n)


def triangle(t, n):
    for i in range(n):
        t.lt(60)
        t.fd(100)
        t.rt(120)
        t.fd(100)
        t.lt(132)
        t.fd(100)
        t.lt(56)


polygon(leo, 5)

turtle.mainloop()