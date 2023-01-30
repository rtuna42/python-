import random
import turtle
import time
delay = 0.15

pencere = turtle.Screen()
pencere.title('Yılan Oyunu')
pencere.bgcolor('lightgreen')
pencere.setup(width=600, height=600)
pencere.tracer(0)

kafa = turtle.Turtle()
kafa.speed(0)
kafa.shape("square")
kafa.color("black")
kafa.penup()
kafa.goto(0, 100)
kafa.direction = "stop"

kafa2 = turtle.Turtle()
kafa2.speed(0)
kafa2.shape("square")
kafa2.color("black")
kafa2.penup()
kafa2.goto(0, -100)
kafa2.direction = "stop"


yemek = turtle.Turtle()
yemek.speed(0)
yemek.shape("circle")
yemek.color("red")
yemek.penup()
yemek.shapesize(0.80, 0.80)
yemek.goto(0, 0)

kuyruklar = []
kuyruklar2 = []
puan = 0


yaz = turtle.Turtle()
yaz.speed(0)
yaz.shape("square")
yaz.color("white")
yaz.penup()
yaz.hideturtle()
yaz.goto(0, 260)
yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))

def move():
    if kafa.direction == "up":
        y = kafa.ycor()
        kafa.sety(y + 20)
    if kafa.direction == "down":
        y = kafa.ycor()
        kafa.sety(y - 20)
    if kafa.direction == "right":
        x = kafa.xcor()
        kafa.setx(x + 20)
    if kafa.direction == "left":
        x = kafa.xcor()
        kafa.setx(x - 20)

    if kafa2.direction == "up":
        y = kafa2.ycor()
        kafa2.sety(y + 20)
    if kafa2.direction == "down":
        y = kafa2.ycor()
        kafa2.sety(y - 20)
    if kafa2.direction == "right":
        x = kafa2.xcor()
        kafa2.setx(x + 20)
    if kafa2.direction == "left":
        x = kafa2.xcor()
        kafa2.setx(x - 20)

def go_up():
    if kafa.direction != "down":
        kafa.direction = "up"
def go_up2():
    if kafa2.direction != "down":
        kafa2.direction = "up"
def go_down():
    if kafa.direction != "up":
        kafa.direction = "down"
def go_down2():
    if kafa2.direction != "up":
        kafa2.direction = "down"





def go_right():
    if kafa.direction != "left":
        kafa.direction = "right"
def go_left():
    if kafa.direction != "right":
        kafa.direction = "left"
def go_right2():
    if kafa2.direction != "left":
        kafa2.direction = "right"
def go_left2():
    if kafa2.direction != "right":
        kafa2.direction = "left"


pencere.listen()
pencere.onkey(go_up, "Up")
pencere.onkey(go_down, "Down")
pencere.onkey(go_right, "Right")
pencere.onkey(go_left, "Left")
pencere.onkey(go_up2, "w")
pencere.onkey(go_down2, "s")
pencere.onkey(go_right2, "d")
pencere.onkey(go_left2, "a")

while True:
    pencere.update()

    if kafa.xcor() > 300 or kafa.xcor() < -300 or kafa.ycor() > 300 or kafa.ycor() < -300:
        time.sleep(1)
        kafa.goto(0, 0)
        kafa.direction = "stop"

        for kuyruk in kuyruklar:
            kuyruk.goto(1000, 1000)
        kuyruklar = []

        puan = 0
        delay = 0.15

        yaz.clear()
        yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))

    if kafa2.xcor() > 300 or kafa2.xcor() < -300 or kafa2.ycor() > 300 or kafa2.ycor() < -300:
        time.sleep(1)
        kafa2.goto(0, 0)
        kafa2.direction = "stop"

        for kuyruk2 in kuyruklar2:
            kuyruk2.goto(1000, 1000)
        kuyruklar2 = []

        puan = 0
        delay = 0.1

        yaz.clear()
        yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))

    if kafa.distance(yemek) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        yemek.goto(x, y)

    if kafa.distance(kafa2)<20:
        kuyruklar.append(yeni_kuyruk)

        




        yeni_kuyruk = turtle.Turtle()
        yeni_kuyruk.speed(0)
        yeni_kuyruk.shape("square")
        yeni_kuyruk.color("white")
        yeni_kuyruk.penup()
        kuyruklar.append(yeni_kuyruk)

        delay -= 0.001

        puan = puan + 10
        yaz.clear()
        yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))

    if kafa2.distance(yemek) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        yemek.goto(x, y)

        yeni_kuyruk2 = turtle.Turtle()
        yeni_kuyruk2.speed(0)
        yeni_kuyruk2.shape("square")
        yeni_kuyruk2.color("white")
        yeni_kuyruk2.penup()
        kuyruklar2.append(yeni_kuyruk2)

        delay -= 0.001

        puan= puan + 10
        yaz.clear()
        yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))

    for index in range(len(kuyruklar) - 1, 0, -1):
        x = kuyruklar[index - 1].xcor()
        y = kuyruklar[index - 1].ycor()
        kuyruklar[index].goto(x, y)

    for index in range(len(kuyruklar2) - 1, 0, -1):
        x = kuyruklar2[index - 1].xcor()
        y = kuyruklar2[index - 1].ycor()
        kuyruklar2[index].goto(x, y)


    if len(kuyruklar) > 0:
        x = kafa.xcor()
        y = kafa.ycor()
        kuyruklar[0].goto(x, y)

    if len(kuyruklar2) > 0:
        x = kafa2.xcor()
        y = kafa2.ycor()
        kuyruklar2[0].goto(x, y)

    move()

    for segment in kuyruklar:
        if segment.distance(kafa) < 20:
            time.sleep(1)
            kafa.goto(0, 0)
            kafa.direction = "stop"
            for segment in kuyruklar:
                segment.goto(1000, 1000)
            kuyruklar = []
            puan = 0
            yaz.clear()
            yaz.write('Puan: {}'.format(puan), align='center', font=('Courier', 24, 'normal'))
            hiz = 0.15

    for segment2 in kuyruklar2:
        if segment2.distance(kafa2) < 20:
            time.sleep(1)
            kafa2.goto(0, 0)
            kafa2.direction = "stop"
            for segment2 in kuyruklar2:
                segment2.goto(1000, 1000)
            kuyruklar2 = []
            puan = 0
            yaz.clear()
            yaz.write('Puan: {}'.format(puan), align='center', font=('Courier', 24, 'normal'))
            hiz2 = 0.15

    time.sleep(delay)