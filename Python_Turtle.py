import turtle

form = turtle.Screen()
kalem = turtle.Turtle()

form.bgcolor("black")
kalem.speed(30)
kalem.pensize(2)

boyutlar = [70,80,90,100,150,200,250,300]


for a in range(len(boyutlar)):

    for i in range(3):

        if i % 2 == 0:

            kalem.color("yellow")
        else:
            kalem.begin_fill()
            kalem.color("blue")
        kalem.left(120)
        kalem.forward(boyutlar[a])

    for i in range(3):

        if i % 2 == 0:
            kalem.color("blue")
        else:
            kalem.color("yellow")
        kalem.right(120)
        kalem.forward(boyutlar[a])

    for i in range(3):

        if i % 2 == 0:
            kalem.color("blue")
        else:
            kalem.color("yellow")
        kalem.forward(boyutlar[a])
        kalem.right(120)

    for i in range(3):

        if i % 2 == 0:
            kalem.color("yellow")
        else:
            kalem.color("blue")
        kalem.forward(boyutlar[a])
        kalem.left(120)

kalem.penup()
kalem.goto(0,350)
kalem.pendown()
kalem.pensize(5)
kalem.color("yellow")
kalem.setheading(180)
kalem.circle(350)

form.mainloop()