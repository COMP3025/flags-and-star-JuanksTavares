import math
import sys

import pygame
from pygame.locals import QUIT

pygame.init()
display = pygame.display.set_mode((500, 300))
white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)
points_triangulo = ((0,0),(250,150),(0,300))
def drawStar(screen, color, position, size, angle):
    points = []
    x, y = position

    for i in range(5):
        pointX = x - size * math.cos((2 * math.pi) * (i / 5) + (math.pi / 2) + angle * math.pi / 180)
        pointY = y - size * math.sin((2 * math.pi) * (i / 5) + (math.pi / 2) + angle * math.pi / 180) 
        
        point = (pointX, pointY)
        points.append(point)

        innerPointX = x - size / 3 * math.cos((2 * math.pi) * (i / 5) + (math.pi / 2) + (2 * math.pi / 10) + angle * math.pi / 180)
        innerPointY = y - size / 3 * math.sin((2 * math.pi) * (i / 5) + (math.pi / 2) + (2 * math.pi / 10) + angle * math.pi / 180)

        innerPoint = (innerPointX, innerPointY)
        points.append(innerPoint)

    pygame.draw.polygon(screen, color, points)


while True:
  drawStar(
    display,(248, 196, 0),(150, 200),50,0)           
  
  display.fill(white)
  pygame.draw.rect(display, blue, pygame.Rect(0, 0, 500, 60))
  pygame.draw.rect(display, blue, pygame.Rect(0, 120, 500, 60))
  pygame.draw.rect(display, blue, pygame.Rect(0, 240, 500, 60))
  pygame.draw.polygon(display, red, points_triangulo)

  drawStar(
    display, 
    white,  
    (90, 150),     
    50,0)               
  
  pygame.display.update()
