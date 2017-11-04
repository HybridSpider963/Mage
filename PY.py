import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)




pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mage")
clock = pygame.time.Clock()


running = True
while running:




    screen.fill(black)
    
