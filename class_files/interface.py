import pygame
from class_files.game import Game
from class_files.classes import Player
import time


class Interface():
    def print_text(screen, message, x, y, font_color=(0, 0, 0), font_type = "", font_size = 0):
        font_type = pygame.font.Font(font_type, font_size)
        text = font_type.render(message, True, font_color)
        screen.blit(text, (x, y))
    def print_stat(screen, player):
        font_color=(0, 0, 0)
        font_type = "fonts/FerdinandFont-Regular.ttf"
        font_size = 25
        font_color=(0, 0, 0)
        font_type = pygame.font.Font(font_type, font_size)
        text = font_type.render("Hp: " + str(player.hp), True, font_color)
        screen.blit(text, (50, 50))
        text = font_type.render("Dmg: " + str(player.damage), True, font_color)
        screen.blit(text, (50, 100))
    
    on = pygame.image.load("img/sound/on.png")
    off = pygame.image.load("img/sound/off.png")
    flPause = False


    class minimap():
        def room_minimap(map, room):

            for i in range(10):
                for j in range(10):

                    if map[i][j] in range(2, 4):
                        pygame.draw.rect(room, (160, 160, 160), (1075 + (j + 1) * 20, 15 + (i + 1) * 20, 17, 17))
                    if map[i][j] == 2 or map[i][j] == 3:
                        if map[i][j - 1] == 1:
                            pygame.draw.rect(room, (96, 96, 96), (1075 + (j) * 20, 15 + (i + 1) * 20, 17, 17))
                        if map[i][j + 1] == 1:
                            pygame.draw.rect(room, (96, 96, 96), (1075 + (j + 2) * 20, 15 + (i + 1) * 20, 17, 17))
                        if map[i - 1][j] == 1:
                            pygame.draw.rect(room, (96, 96, 96), (1075 + (j + 1) * 20, 15 + (i) * 20, 17, 17))
                        if map[i + 1][j] == 1:
                            pygame.draw.rect(room, (96, 96, 96), (1075 + (j + 1) * 20, 15 + (i + 2) * 20, 17, 17))

                        if map[i][j - 1] == 4:
                            pygame.draw.rect(room, "Red", (1075 + (j) * 20, 15 + (i + 1) * 20, 17, 17))
                        if map[i][j + 1] == 4:
                            pygame.draw.rect(room, "Red", (1075 + (j + 2) * 20, 15 + (i + 1) * 20, 17, 17))
                        if map[i - 1][j] == 4:
                            pygame.draw.rect(room, "Red", (1075 + (j + 1) * 20, 15 + (i) * 20, 17, 17))
                        if map[i + 1][j] == 4:
                            pygame.draw.rect(room, "Red", (1075 + (j + 1) * 20, 15 + (i + 2) * 20, 17, 17))

                        if map[i][j - 1] == 5:
                            pygame.draw.rect(room, "Gold", (1075 + (j) * 20, 15 + (i + 1) * 20, 17, 17))
                        if map[i][j + 1] == 5:
                            pygame.draw.rect(room, "Gold", (1075 + (j + 2) * 20, 15 + (i + 1) * 20, 17, 17))
                        if map[i - 1][j] == 5:
                            pygame.draw.rect(room, "Gold", (1075 + (j + 1) * 20, 15 + (i) * 20, 17, 17))
                        if map[i + 1][j] == 5:
                            pygame.draw.rect(room, "Gold", (1075 + (j + 1) * 20, 15 + (i + 2) * 20, 17, 17))

                    

        def player_minimap(map, room):
            for i in range(10):
                for j in range(10):
                    if map[i][j] == 2:
                        pygame.draw.rect(room, "Green", (1078 + (j + 1) * 20, 18 + (i + 1) * 20, 11, 11))

    class room():
        D = "img/rooms/d.jpeg"
        DL = "img/rooms/dl.jpeg"
        L = "img/rooms/l.jpeg"
        R = "img/rooms/r.jpeg"
        RD = "img/rooms/rd.jpeg"
        RDL = "img/rooms/rdl.jpeg"
        RL = "img/rooms/rl.jpeg"
        U = "img/rooms/u.jpeg"
        UD = "img/rooms/ud.jpeg"
        UDL = "img/rooms/udl.jpeg"
        UL = "img/rooms/ul.jpeg"
        UR = "img/rooms/ur.jpeg"
        URD = "img/rooms/urd.jpeg"
        URL = "img/rooms/url.jpeg"
        URDL = "img/rooms/urdl.jpeg"

        def room_changing(player, map, room_x, room_y, room): 

            if player.x < 226 and map[room_x][room_y - 1] != 0:
                if map[room_x][room_y] not in range(4, 6):
                    map[room_x][room_y] = 3
                map[room_x][room_y - 1] = 2
                room_y -= 1
                img = Game.map.room_choose(map, room_x, room_y)
                room = pygame.image.load(img)
                player.x = 965
                player.y = 408
                Interface.minimap.player_minimap(map, room)

            if player.x > 1000 and map[room_x][room_y + 1] != 0:
                if map[room_x][room_y] not in range(4, 6):
                    map[room_x][room_y] = 3

                map[room_x][room_y + 1] = 2
                room_y += 1
                img = Game.map.room_choose(map, room_x, room_y)
                room = pygame.image.load(img)
                player.x = 258
                player.y = 418
                Interface.minimap.player_minimap(map, room)

            if player.y < 195 and map[room_x - 1][room_y] != 0:
                if map[room_x][room_y] not in range(4, 6):
                    map[room_x][room_y] = 3
                map[room_x - 1][room_y] = 2
                room_x -= 1
                img = Game.map.room_choose(map, room_x, room_y)
                room = pygame.image.load(img)
                player.x = 611
                player.y = 603
                Interface.minimap.player_minimap(map, room)

            if player.y > 640 and map[room_x + 1][room_y] != 0:
                if map[room_x][room_y] not in range(4, 6):
                    map[room_x][room_y] = 3
                map[room_x + 1][room_y] = 2
                room_x += 1
                img = Game.map.room_choose(map, room_x, room_y)
                room = pygame.image.load(img)
                player.x = 604
                player.y = 224
                Interface.minimap.player_minimap(map, room)

            
            return room, room_x, room_y
        

    class menu():
        def player_choose(screen, running):

            menu = pygame.image.load("img/menu/main_menu.jpg")
            vanechka = pygame.image.load("img/players/big/vanechka.png")
            shaman = pygame.image.load("img/players/big/shaman.png")
            dimochka = pygame.image.load("img/players/big/dimochka.png")

            dimochka_small = pygame.image.load("img/players/dimochka.png")
            vanechka_small = pygame.image.load("img/players/vanechka.png")
            shaman_small = pygame.image.load("img/players/shaman.png")




            choose = 1

            while running:
                screen.blit(menu, (0, 0))

                if not Interface.flPause:
                    screen.blit(Interface.on, (10, 10))
                else:
                    screen.blit(Interface.off, (10, 10))

                Interface.print_text(screen, "Choose a player", 200, 70, "Brown", "fonts/SuperWebcomicBros_Rusbyyakustick_-Regular_0.ttf", 45)
                Interface.print_text(screen, "The Legend of ACSiE", 800, 70, "Brown", "fonts/FerdinandFont-Regular.ttf", 45)
                Interface.print_text(screen, "Tears of students", 860, 120, "Brown", "fonts/FerdinandFont-Regular.ttf", 35)

                screen.blit(vanechka, (100, 300))
                screen.blit(dimochka, (500, 249))
                screen.blit(shaman, (950, 200))

                if choose == 0:
                    pygame.draw.rect(screen, "Light Green", (100, 300, 200, 200), 5)
                elif choose == 1:
                    pygame.draw.rect(screen, "Light Green", (500, 249, 250, 251), 5)
                elif choose == 2:
                    pygame.draw.rect(screen, "Light Green", (950, 200, 200, 300), 5)

                Interface.print_text(screen, "HP: ||", 165, 510, "White", "fonts/FerdinandFont-Regular.ttf", 25)
                Interface.print_text(screen, "DMG: ||||", 165, 540, "White", "fonts/FerdinandFont-Regular.ttf", 25)
                Interface.print_text(screen, "HP: |||", 600, 510, "White", "fonts/FerdinandFont-Regular.ttf", 25)
                Interface.print_text(screen, "DMG: |||", 600, 540, "White", "fonts/FerdinandFont-Regular.ttf", 25)
                Interface.print_text(screen, "HP: ||||", 1015, 510, "White", "fonts/FerdinandFont-Regular.ttf", 25)
                Interface.print_text(screen, "DMG: ||", 1015, 540, "White", "fonts/FerdinandFont-Regular.ttf", 25)

                

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_m:
                            Interface.flPause = not Interface.flPause
                            if Interface.flPause:
                                pygame.mixer.music.pause()
                            else:
                                pygame.mixer.music.unpause()
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            if choose == 1:
                                choose = 0
                            elif choose == 2:
                                choose = 1
                            else:
                                choose = 2
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            if choose == 1:
                                choose = 2
                            elif choose == 2:
                                choose = 0
                            else:
                                choose = 1   

                        if event.key == pygame.K_SPACE:
                            print(choose)
                            if choose == 0:
                                player = Player(vanechka_small, None, 2, 4, 0.9, 0.6, None, 540, 300)            
                                Interface.game.main_game(screen, player)
                            elif choose == 1:
                                player = Player(dimochka_small, None, 3, 3, 0.9, 0.6, None, 540, 300) 
                                Interface.game.main_game(screen, player)
                            else:
                                player = Player(shaman_small, None, 4, 2, 0.9, 0.6, None, 540, 300)
                                Interface.game.main_game(screen, player)

                pygame.display.update()


        def main_menu(screen, running):

            pygame.mixer.music.load("music/main.mp3")
            pygame.mixer.music.play(-1)
            FPS = 15
            direct_y = 1
            clock = pygame.time.Clock()

            menu = pygame.image.load("img/menu/main_menu.jpg")
            y = 540

            while running:
                clock.tick(FPS)
                screen.blit(menu, (0, 0))
                
                if not Interface.flPause:
                    screen.blit(Interface.on, (10, 10))
                else:
                    screen.blit(Interface.off, (10, 10))

                Interface.print_text(screen, "The Legend of ACSiE", 800, 70, "Brown", "fonts/FerdinandFont-Regular.ttf", 45)
                Interface.print_text(screen, "Tears of students", 860, 120, "Brown", "fonts/FerdinandFont-Regular.ttf", 35)

                Interface.print_text(screen, "Press SPACE to START", 430, y, "Grey", "fonts/SuperWebcomicBros_Rusbyyakustick_-Regular_0.ttf", 45) 
                y += direct_y

                if y > 545 or y < 535:
                    direct_y = -direct_y

                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_m:
                            Interface.flPause = not Interface.flPause
                            if Interface.flPause:
                                pygame.mixer.music.pause()
                            else:
                                pygame.mixer.music.unpause()
                        if event.key == pygame.K_SPACE:
                            Interface.menu.player_choose(screen, running)

                

    class game():
        def main_game(screen, player):
            room_x = 4
            room_y = 4
            running = True

            player.hitbox = player.texture.get_rect(topleft = (player.x, player.y))

            map = Game.map.rand_map()
            room = pygame.image.load(Game.map.room_choose(map, room_x, room_y))


            while running:
                
                Interface.minimap.room_minimap(map, room)
                Interface.minimap.player_minimap(map, room)

                room, room_x, room_y = Interface.room.room_changing(player, map, room_x, room_y, room)

                screen.blit(room, (0, 0))

                screen.blit(player.texture, (player.x, player.y))
                Player.moving(player)
                
                Interface.print_stat(screen, player)
                
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_m:
                            Interface.flPause = not Interface.flPause
                            if Interface.flPause:
                                pygame.mixer.music.pause()
                            else:
                                pygame.mixer.music.unpause()


