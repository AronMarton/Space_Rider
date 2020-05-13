import turtle
import pygame

pygame.mixer.init()
pygame.mixer.music.load('C:\\Users\\Aron\\Desktop\\bgsound.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

screen = turtle.Screen()
screen.title('Space Rider')
screen.setup(900,650)
image = "C:\\Users\\Aron\\Desktop\\Python\\spaceship_gif.gif"

screen.addshape(image)
turtle.shape(image)

screen.bgpic('C:\\Users\\Aron\\Desktop\\Python\\space_gif.gif')


def k1():
    turtle.forward(3)

def k2():
    turtle.backward(3)

def k3():
    turtle.left(20)

def k4():
    turtle.right(20)

turtle.penup()
turtle.speed(0)
turtle.home()

turtle.onkeypress(k1, 'Right')
turtle.onkeypress(k2, 'Left')
turtle.onkeypress(k3, 'Up')
turtle.onkeypress(k4, 'Down')
turtle.listen()

screen.mainloop()   