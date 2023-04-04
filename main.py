import pygame
from class_files.interface import Interface
from const import WIDTH, HEIGHT, running

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FEFUgame")
icon = pygame.image.load("img/icons/icon.png")
pygame.display.set_icon(icon)


Interface.intro(screen, running)
        
            