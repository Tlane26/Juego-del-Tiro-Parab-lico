#En este juego se trata de que cuando el ususario accione el juego este vea diferentes onjetivos y con su cañon sea capaz
#de disparar multiples veces a objetivos que apareccen continuamente con un cañon de disparo parabolico, el programa tiene
#cierta dificultad debido al tamaño de los objetivos y la bala de cañon, ademas de que la velocidad de este complica el juego
#añadiendo que el proyectil tiene una parabola haciendo imposible el tener un disparo directo
from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw(): # Esta funcion es la que nos va sacando las balas y los objetivos del area para que sean visibles
    "Draw ball and targets."
    clear()

    for target in targets:# Aqui procede a representar lo que se elimina ya codeado anteriormente y en esta seccion solo se visualiza el como se veria el objetivo cualquier cambio aqui no tiene un efecto en el funcionamiento de esta.
        goto(target.x, target.y)
        dot(20, 'blue') # Este es el cambio del punto objetico de tamaño y su color por lo cual modificando esas cualidades puedes cambiar su tamaño aunque eso no significa que toda su area sea valida

    if inside(ball): # La bola de cañon se presenta aqui y se trae lo que la bola es capaz de hacer puesto previamente solo que aqui se trabaja el aspecto fisco de la bola
        goto(ball.x, ball.y)
        dot(10, 'red') # Cambio de tamaño y color de la bola de cañon la cual fue cambiada para hacer algo mas grande 

    update()

def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            target.x = 205
            
    ontimer(move, 25) # Para llamar la funcion move este tiempo aumenta la velocidad del programa con un tiempom de 25milisegundos y aumentando esta el programa corre mas rapido o lento dependiendo de lo añadido

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
