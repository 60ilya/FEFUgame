import pygame
import class_files.classes as classes
from class_files.interface import Interface
from class_files.game import Game
from const import room_x, room_y, WIDTH, HEIGHT, running

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # flags = pygame.NOFRAME
pygame.display.set_caption("FEFUgame")
icon = pygame.image.load("img/icons/icon.png")
pygame.display.set_icon(icon)


Interface.menu.main_menu(screen, running)
# Interface.game.main_game(screen)
# Interface.boss_battle(screen)
        
            