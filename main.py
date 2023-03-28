import pygame
import class_files.classes as classes
from class_files.interface import Interface
from class_files.game import Game
from const import WIDTH, HEIGHT, running

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # flags = pygame.NOFRAME
pygame.display.set_caption("FEFUgame")
icon = pygame.image.load("img/icons/icon.png")
pygame.display.set_icon(icon)


Interface.intro(screen, running)
        
            