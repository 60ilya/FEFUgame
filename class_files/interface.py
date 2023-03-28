import pygame
from pyvidplayer import Video
from class_files.game import Game
from class_files.classes import Player, SpeedBoost, HealthPotion, DamageBoost, Item, Archer, Arrow, Mob
from const import door_up, door_down, door_left, door_right
import random


class Interface():

    on = pygame.image.load("img/sound/on.png")
    off = pygame.image.load("img/sound/off.png")
    flPause = False

    def print_text(screen, message, x, y, font_color=(0, 0, 0), font_type = "", font_size = 0):
        font_type = pygame.font.Font(font_type, font_size)
        text = font_type.render(message, True, font_color)
        screen.blit(text, (x, y))

    def print_stat(screen, player):
        Interface.print_text(screen, "hp", 50, 50, "Red", "fonts/SuperWebcomicBros_Rusbyyakustick_-Regular_0.ttf", 70)
        
        for i in range(player.hp):
            screen.blit(player.texture, (120 + i*80, 50))
        Interface.print_text(screen, "dmg", 30, 340, "Yellow", "fonts/SuperWebcomicBros_Rusbyyakustick_-Regular_0.ttf", 30)
        Interface.print_text(screen, "spd", 30, 300, "Yellow", "fonts/SuperWebcomicBros_Rusbyyakustick_-Regular_0.ttf", 30)
        Interface.print_text(screen, f"{player.damage}", 100, 340, "White", "fonts/SuperWebcomicBros_Rusbyyakustick_-Regular_0.ttf", 40)
        Interface.print_text(screen, f"{player.speed}", 100, 300, "White", "fonts/SuperWebcomicBros_Rusbyyakustick_-Regular_0.ttf", 40)  

    def intro(screen, running):
        intro2 = Video("video/intro_max.mp4")
        intro2.set_size((1280, 768)) 
        flag = True
        

        while running:
            if intro2.active == False:
                Interface.menu.main_menu(screen, running)

            intro2.draw(screen, (0, 0))

            Interface.print_text(screen, "Press SPACE to skip intro", 900, 0, "Grey", "fonts/SuperWebcomicBros_Rusbyyakustick_-Regular_0.ttf", 30) 
            

            pygame.display.update()

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            intro2.close()
                            Interface.menu.main_menu(screen, running)

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

        def room_changing(player, map, room_x, room_y, room, bullets: list): 
            if player.x < 226 and map[room_x][room_y - 1] != 0:
                bullets.clear()
                if map[room_x][room_y] not in range(4, 6):
                    map[room_x][room_y] = 3
                map[room_x][room_y - 1] = 2
                room_y -= 1
                img = Game.map.room_choose(map, room_x, room_y)
                room = pygame.image.load(img)
                player.x = 965
                player.y = 408
                Interface.minimap.player_minimap(map, room)
                for i in range(10):
                    print(map[i])

            if player.x > 1000 and map[room_x][room_y + 1] != 0:
                bullets.clear()
                if map[room_x][room_y] not in range(4, 6):
                    map[room_x][room_y] = 3

                map[room_x][room_y + 1] = 2
                room_y += 1
                img = Game.map.room_choose(map, room_x, room_y)
                room = pygame.image.load(img)
                player.x = 258
                player.y = 418
                Interface.minimap.player_minimap(map, room)
                for i in range(10):
                    print(map[i])

            if player.y < 195 and map[room_x - 1][room_y] != 0:
                bullets.clear()
                if map[room_x][room_y] not in range(4, 6):
                    map[room_x][room_y] = 3
                map[room_x - 1][room_y] = 2
                room_x -= 1
                img = Game.map.room_choose(map, room_x, room_y)
                room = pygame.image.load(img)
                player.x = 611
                player.y = 603
                Interface.minimap.player_minimap(map, room)
                for i in range(10):
                    print(map[i])

            if player.y > 640 and map[room_x + 1][room_y] != 0:
                bullets.clear()
                if map[room_x][room_y] not in range(4, 6):
                    map[room_x][room_y] = 3
                map[room_x + 1][room_y] = 2
                room_x += 1
                img = Game.map.room_choose(map, room_x, room_y)
                room = pygame.image.load(img)
                player.x = 604
                player.y = 224
                Interface.minimap.player_minimap(map, room)
                for i in range(10):
                    print(map[i])

            
            return room, room_x, room_y
        
        def init_treasure_room(map, screen):
            tx, ty = 0, 0

            for y in range(10):
                for x in range(10):
                    if map[x][y] == 5:
                        tx, ty = x, y

            item1 = SpeedBoost("img/items/1.png")
            item2 = HealthPotion("img/items/2.png")
            item3 = DamageBoost("img/items/3.png")
            item4 = DamageBoost("img/items/4.png")
            item5 = HealthPotion("img/items/5.png")
          
            item1.texture = pygame.image.load(item1.texture)          
            item2.texture = pygame.image.load(item2.texture)         
            item3.texture = pygame.image.load(item3.texture)          
            item4.texture = pygame.image.load(item4.texture)
            item5.texture = pygame.image.load(item5.texture)

            item_list = [item1, item2, item3, item4, item5]
            main_item = random.choice(item_list)

            return tx, ty, main_item
        
        def get_mobs_rooms(map, screen):
            room_with_mobs = []
            for y in range(10):
                for x in range(10):
                    if map[x][y] == 1:
                        room_with_mobs.append([x, y])
            print(room_with_mobs)
            
            return room_with_mobs

        
        

    class menu():
        def player_choose(screen, running):

            menu = pygame.image.load("img/menu/main_menu.jpg")
            vanechka = pygame.image.load("img/players/big/vanechka.png")
            shaman = pygame.image.load("img/players/big/shaman.png")
            dimochka = pygame.image.load("img/players/big/dimochka.png")

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
                            Interface.game.main_game(screen, choose)

                        if event.key == pygame.K_ESCAPE:
                            Interface.menu.main_menu(screen, running)

                pygame.display.update()


        def main_menu(screen, running):

            pygame.mixer.music.load("music/main.mp3")
            pygame.mixer.music.play(-1)

            FPS = 60
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

                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            

                

    class game():
        def main_game(screen, choose):
            room_x = 4
            room_y = 4
            running = True
            
            if choose == 0:
                vanechka_small = pygame.image.load("img/players/vanechka.png")
                player = Archer(vanechka_small, None, 2, 4, 1.5, 1.2, False, 540, 300, False)            
            elif choose == 1:
                dimochka_small = pygame.image.load("img/players/dimochka.png")
                player = Archer(dimochka_small, None, 3, 3, 1.5, 1.2, False, 540, 300, False) 
            else:
                shaman_small = pygame.image.load("img/players/shaman.png")
                player = Archer(shaman_small, None, 4, 2, 1.5, 1.2, False, 540, 300, False)

            

            map = Game.map.rand_map()
            room = pygame.image.load(Game.map.room_choose(map, room_x, room_y))
            cats = pygame.image.load("img/enemy/mobs/cats.png")
            egg = pygame.image.load("img/shoot/egg.png")

            mob1 = Mob(50, 1, cats, 2, 580, 470, None)
            mob2 = Mob(50, 1, cats, 2, 510, 400, None)
            mob3 = Mob(50, 1, cats, 2, 650, 400, None)
            mob4 = Mob(50, 1, cats, 2, 580, 330, None)

            mobs_list = [mob1, mob2, mob3, mob4]

            

            gold_x, gold_y, item = Interface.room.init_treasure_room(map, screen)
            item_hitbox = item.texture.get_rect(topleft = (570, 400))

            mobs_room = Interface.room.get_mobs_rooms(map, screen)
            

            bullets = []

            while running:
                xy = player.room_coordinates(map)

                player.hitbox = player.texture.get_rect(topleft = (player.x, player.y))

                Game.map.room_inv_block(map, room_x, room_y, player)
                
                Interface.minimap.room_minimap(map, room)
                Interface.minimap.player_minimap(map, room)

                room, room_x, room_y = Interface.room.room_changing(player, map, room_x, room_y, room, bullets)

                screen.blit(room, (0, 0))

                screen.blit(player.texture, (player.x, player.y))
                player.moving()
                
                Interface.print_stat(screen, player)

                Mob.spawn(map, screen, xy, mobs_room, mob1, mob2, mob3, mob4, mobs_list)


                Item.create_item(gold_x, gold_y, map, item.texture, screen, player)
                Item.collision(item_hitbox, player, gold_x, gold_y, map, item)
                
                player.shooting(bullets, screen, egg)

                
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
                        if event.key == pygame.K_r:
                            Interface.game.main_game(screen, choose)
                        
                        if event.key == pygame.K_ESCAPE:
                            Interface.menu.main_menu(screen, running)
                        
                        if event.key == pygame.K_LEFT:
                            if len(bullets) < 5:
                                bullets.append(Arrow(player.x + 35, player.y + 35, "a"))

                        if event.key == pygame.K_RIGHT:
                            if len(bullets) < 5:
                                bullets.append(Arrow(player.x + 35, player.y + 35, "d"))
                            
                        if event.key == pygame.K_UP:
                            if len(bullets) < 5:
                                bullets.append(Arrow(player.x + 35, player.y + 35, "w"))
                                
                        if event.key == pygame.K_DOWN:
                            if len(bullets) < 5:
                                bullets.append(Arrow(player.x + 35, player.y + 35, "s"))
                            


