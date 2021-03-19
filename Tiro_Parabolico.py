#Tlanetzi Chávez Madero 			A00830340
#Luis Daniel Piña Maldonado	            A01284406
#En este juego se trata de que cuando el ususario accione el juego este vea diferentes onjetivos y con su cañon sea capaz
#de disparar multiples veces a objetivos que apareccen continuamente con un cañon de disparo parabolico, el programa tiene
#cierta dificultad debido al tamaño de los objetivos y la bala de cañon, ademas de que la velocidad de este complica el juego
#añadiendo que el proyectil tiene una parabola haciendo imposible el tener un disparo directo
from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200) # Posicion origianl de ball
speed = vector(0, 0) # Velocidad inicial
targets = [] #Arrego de targets, aqui se iran incorporando los nuevos objetos creados

def tap(x, y): # Funcion que recibe como parametros la posicion x y y del cursor 
    "Respond to screen tap."
    if not inside(ball): # Si ball no se encuentra en los limites se le asiganran valores default
        ball.x = -199 #Posicion en x
        ball.y = -199 #Posicion en y
        speed.x = (x + 200) / 25 #Vector que simula la velocidad en x
        speed.y = (y + 200) / 25 #Vector que simula la velocidad en y

def inside(xy): #Funcion para concer si la posicion del objeto se encuentra en la ventana de juego
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200 #Limites de la ventana de juego

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

def move(): #Funcion para el movimiento de ball y los targets
    "Move ball and targets."
    if randrange(40) == 0: # If que funciona para generar de manera aleatoria los targets
        y = randrange(-150, 150) # Asigna un valor random entre -150 a 150 para y
        target = vector(200, y) # Le asigna el valor random a target en y  
        targets.append(target) # Se agrega este nuevo objeto al arreglo de targets

    for target in targets: # Aplica para todos los objetos del arreglo targets
        target.x -= 10 # Modifica la posicion en x de cada objeto
        
    if inside(ball): # verifica que ball este en la ventana de juego
        speed.y -= 0.40 # si ball esta dentro de los limites, se va restando el valor en y
        ball.move(speed) # Mueve ball en funcion del vector speed

    dupe = targets.copy() # Copia el arreglo targets
    targets.clear() # Borra los objetos del arreglo targets

    for target in dupe: # Determina para los objetos target en dupe
        if abs(target - ball) > 13: # Si el valor abosluto es mayor a cierta distancia entre ball y target ...
            targets.append(target) # Se agrega de nuevo el objeto al arreglo targets
            # Sirve para definir si los objetos fueron 'eliminados' por ball

    draw() # Dibuja los circulos en la ventana de juego

    for target in targets: #Se evaluara el target
        if not inside(target): # Si este se encuentra en el limite de la ventana de juego...
            target.x = 205 # Su posicion cambiara al limite derecho para que aparezca de nuevo en el juego

            
    ontimer(move, 25) # Para llamar la funcion move este tiempo aumenta la velocidad del programa con un tiempom de 25milisegundos y aumentando esta el programa corre mas rapido o lento dependiendo de lo añadido

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
