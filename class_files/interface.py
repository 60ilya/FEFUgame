import pygame
from pyvidplayer import Video
from class_files.game import Game
from class_files.classes import SpeedBoost, HealthPotion, DamageBoost, Item, Archer, Arrow, Boss, Mob
from const import door_up, door_down, door_left, door_right, door_up_open, door_down_open, door_left_open, door_right_open
from const import mov_right, mov_left, shoot_down, shoot_left, shoot_right, shoot_up
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
            screen.blit(player.texture, (120 + i * 80, 50))
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
    #миникарта
    class minimap():

        def room_minimap(map, room, gold_x, gold_y, boss_x, boss_y, room_x, room_y):
            
            pygame.draw.rect(room, (96, 96, 96), (1065, 5, 205, 205), 10, 10)    
            
            for i in range(10):
                for j in range(10):

                    if map[i][j] in range(2, 4):
                        pygame.draw.rect(room, (160, 160, 160), (1075 + (j + 1) * 20, 15 + (i + 1) * 20, 17, 17))
                    if map[i][j] == 2:
                        if room_x == gold_x and room_y == gold_y:
                            pygame.draw.rect(room, "Gold", (1075 + (j + 1) * 20, 15 + (i + 1) * 20, 17, 17))
                            
                        elif room_x == boss_x and room_y == boss_y:
                            pygame.draw.rect(room, "Red", (1075 + (j + 1) * 20, 15 + (i + 1) * 20, 17, 17))
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

        door_hor = pygame.image.load("img/doors/horizontal.png")
        door_ver = pygame.image.load("img/doors/vertical.png")

        def room_changing(player, map, room_x, room_y, room, bullets, mobs_list, mob1, mob2, mob3, mob4, mobs_room): 
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
                if [room_x, room_y] in mobs_room: 
                    mobs_list.extend([mob1, mob2, mob3, mob4])
                    print(mob1.hp, mob2.hp, mob3.hp, mob4.hp)
                for i in range(10):
                    print(map[i])
                print()
                

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
                if [room_x, room_y] in mobs_room: 
                    mobs_list.extend([mob1, mob2, mob3, mob4])
                    print(mob1.hp, mob2.hp, mob3.hp, mob4.hp)
                for i in range(10):
                    print(map[i])
                print()

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
                if [room_x, room_y] in mobs_room: 
                    mobs_list.extend([mob1, mob2, mob3, mob4])
                    print(mob1.hp, mob2.hp, mob3.hp, mob4.hp)
                for i in range(10):
                    print(map[i])
                print()

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
                if [room_x, room_y] in mobs_room: 
                    mobs_list.extend([mob1, mob2, mob3, mob4])
                    print(mob1.hp, mob2.hp, mob3.hp, mob4.hp)
                for i in range(10):
                    print(map[i])
                print()

            
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
            
            return room_with_mobs
        
        def block_rooms(mobs_list, player, screen, vertical, horizontal, map, x, y, boss_x, boss_y):
            if len(mobs_list) != 0 or (x == boss_x and y == boss_y):
                
                if player.y < 222:
                    player.y = 223
                    
                if player.y > 614:
                    player.y = 613

                if player.x < 244:
                    player.x = 245

                if player.x > 972:
                    player.x = 971

                if map[x][y - 1] != 0:
                    screen.blit(vertical, door_left)
                if map[x][y + 1] != 0:
                    screen.blit(vertical, door_right)
                if map[x + 1][y] != 0:
                    screen.blit(horizontal, door_down)
                if map[x - 1][y] != 0:
                    screen.blit(horizontal, door_up)
            
            else:
                if map[x][y - 1] != 0:
                    screen.blit(vertical, door_left_open)
                if map[x][y + 1] != 0:
                    screen.blit(vertical, door_right_open)
                if map[x + 1][y] != 0:
                    screen.blit(horizontal, door_down_open)
                if map[x - 1][y] != 0:
                    screen.blit(horizontal, door_up_open)

        
        
    #главная заставка + выбор персонажа
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
                        if event.key == shoot_left or event.key == mov_left:
                            if choose == 1:
                                choose = 0
                            elif choose == 2:
                                choose = 1
                            else:
                                choose = 2
                        if event.key == shoot_right or event.key == mov_right:
                            if choose == 1:
                                choose = 2
                            elif choose == 2:
                                choose = 0
                            else:
                                choose = 1   

                        if event.key == pygame.K_SPACE:
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
            #создание персонажа
            if choose == 0:
                vanechka_small = pygame.image.load("img/players/vanechka.png")
                player = Archer(vanechka_small, None, 2, 4, 1.5, 1.2, False, 540, 300, False)            
            elif choose == 1:
                dimochka_small = pygame.image.load("img/players/dimochka.png")
                player = Archer(dimochka_small, None, 3, 10, 1.5, 1.2, False, 540, 300, False) 
            else:
                shaman_small = pygame.image.load("img/players/shaman.png")
                player = Archer(shaman_small, None, 4, 2, 1.5, 1.2, False, 540, 300, False)

            

            map = Game.map.rand_map()
            room = pygame.image.load(Game.map.room_choose(map, room_x, room_y))
            cats = pygame.image.load("img/enemy/mobs/cats.png")
            egg = pygame.image.load("img/shoot/egg.png")

            door_hor = pygame.image.load("img/doors/horizontal.png")
            door_ver = pygame.image.load("img/doors/vertical.png")

            mob1 = Mob(10, 1, cats, 0.5, 580, 410, None, "d")
            mob2 = Mob(10, 1, cats, 0.5, 510, 400, None, "l")
            mob3 = Mob(10, 1, cats, 0.5, 650, 400, None, "r")
            mob4 = Mob(10, 1, cats, 0.5, 580, 390, None, "u")

            boss = Boss(pygame.image.load("img/boss/klunin5.png"), 10, 1, 0.5, 500, 300)

            

            gold_x, gold_y, item = Interface.room.init_treasure_room(map, screen)#корды предметов
            item_hitbox = item.texture.get_rect(topleft = (570, 400))#текстуры предметов

            boss_x, boss_y = Game.map.get_boss_xy(map)

            mobs_room = Interface.room.get_mobs_rooms(map, screen)
            
            mobs_list = []
            
            bullets = []
            block = 0

            while running:
                
                player.hitbox = player.texture.get_rect(topleft = (player.x, player.y))

                Game.map.room_inv_block(map, room_x, room_y, player)
                
                Interface.minimap.room_minimap(map, room, gold_x, gold_y, boss_x, boss_y, room_x, room_y)
                Interface.minimap.player_minimap(map, room)
                

                room, room_x, room_y = Interface.room.room_changing(player, map, room_x, room_y, room, bullets, mobs_list, mob1, mob2, mob3, mob4, mobs_room)

                screen.blit(room, (0, 0))

                screen.blit(player.texture, (player.x, player.y))
                if block == 0:
                    player.moving()
                
                Mob.spawn(map, screen, [room_x, room_y], mobs_room, mob1, mob2, mob3, mob4, mobs_list)
                Mob.get_hitbox(mobs_list)
                Mob.move_towards_player(mobs_list, player)
                

                Interface.room.block_rooms(mobs_list, player, screen, door_ver, door_hor, map, room_x, room_y, boss_x, boss_y)
                

                player.shooting(bullets, screen, egg)
                Arrow.get_hitbox(bullets)


                Interface.print_stat(screen, player)

                
                Mob.collision(player, mobs_list, bullets)
                Mob.collision_player(mobs_list, player)
                Mob.collide_each_other(mobs_list)
                # Mob.hp_box(mobs_list, room)

                Item.create_item(gold_x, gold_y, map, item.texture, screen, player)
                Item.collision(item_hitbox, player, gold_x, gold_y, map, item)

# Действия в комнате босса
                if room_x==boss_x and room_y==boss_y:
                    block = 1
                    Boss.spawn(map, screen, boss)
                    Boss.get_hitbox(boss)
                    Boss.move_towards_player(boss, player)
                    if player.hitbox.colliderect(boss.hitbox):
                        pygame.mixer.music.pause()
                        Interface.game.boss_fight(screen, player, running)
# Смерть
                if player.hp <= 0:
                    Interface.print_text(screen, "YOU DIED", 400, 350, "Red", "fonts/SuperWebcomicBros_Rusbyyakustick_-Regular_0.ttf", 150)
                    block = 1
                    Interface.print_text(screen, "Press SPACE to continue", 430, 450, "Grey", "fonts/SuperWebcomicBros_Rusbyyakustick_-Regular_0.ttf", 45)
                    pygame.mixer.music.pause()

                
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_m  and block == 0:
                            Interface.flPause = not Interface.flPause
                            if Interface.flPause:
                                pygame.mixer.music.pause()
                            else:
                                pygame.mixer.music.unpause()

                        if player.hp<=0 and (event.key == pygame.K_RETURN or event.key == pygame.K_SPACE):
                            Interface.game.boss_fight(screen, player, running)

                        if event.key == pygame.K_r:
                            pygame.mixer.music.play(-1)
                            Interface.game.main_game(screen, choose)

                        if event.key == pygame.K_b: #временное включение босса
                            pygame.mixer.music.pause()
                            Interface.game.boss_fight(screen, player, running)
                        
                        if event.key == pygame.K_ESCAPE:
                            Interface.menu.main_menu(screen, running)
                        
                        if event.key == shoot_left and block == 0:
                            if len(bullets) < 5:
                                bullets.append(Arrow(player.x + 35, player.y + 35, "a", egg))

                        if event.key == shoot_right and block == 0:
                            if len(bullets) < 5:
                                bullets.append(Arrow(player.x + 35, player.y + 35, "d", egg))
                            
                        if event.key == shoot_up and block == 0:
                            if len(bullets) < 5:
                                bullets.append(Arrow(player.x + 35, player.y + 35, "w", egg))
                                
                        if event.key == shoot_down and block == 0:
                            if len(bullets) < 5:
                                bullets.append(Arrow(player.x + 35, player.y + 35, "s", egg))


        def boss_fight(screen, player, running):
            
            boss = Boss(pygame.image.load("img/boss/klunin5.png"), 5, 1, None, 500, 100)

            def print_boss(hp):
                if hp == 5:
                    screen.blit(bigboss, (0, 100))
                elif hp == 4:
                    screen.blit(bigboss1, (0, 100))
                elif hp == 3:
                    screen.blit(bigboss2, (0, 100))
                elif hp == 2:
                    screen.blit(bigboss3, (0, 100))
                elif hp == 1:
                    screen.blit(bigboss4,(0, 100))
                else:
                    screen.blit(bigboss,(0, 100))

            pygame.init()

            bg = pygame.image.load("img/boss/menu1.jpg")

            badtest = pygame.image.load("img/boss/badtest.png")
            goodtest = pygame.image.load("img/boss/goodtest.png")
            bigboss = pygame.image.load("img/boss/boss1.png")
            bigboss1 = pygame.image.load("img/boss/boss2.png")
            bigboss2 = pygame.image.load("img/boss/boss3.png")
            bigboss3 = pygame.image.load("img/boss/boss5.png")
            bigboss4 = pygame.image.load("img/boss/boss6.png")
            dvfu = pygame.image.load("img/boss/dvfu.png")
            block = pygame.image.load("img/boss/block2.png")


            square = pygame.Surface((430, 65))
            square.fill("White")
            mainsound = pygame.mixer.Sound("music/battle_music.mp3")

            main_string1 = pygame.font.Font("fonts/SuperWebcomicBros_Rusbyyakustick_-Regular_0.ttf", 40)
            string2 = main_string1.render("Вы готовы к бою?", False, "White")
            string3 = main_string1.render("Нажмите ENTER, чтобы начать ", False, "White")
            string4 = main_string1.render("Нажмите SPACE ,чтобы сбежать ", False, "White", "Black")

            badend = False
            
            test = False
            answ = True
            question = True
            endgame = False
            q = 1


            while True:

                mainsound.play()

                screen.blit(bg,(0,0))

                if not(test) and not(endgame):
                    screen.blit(string2, (150, 360))
                    screen.blit(string3, (150, 410))
                    screen.blit(string4, (150, 460))

                if test:
                    
                    screen.blit(dvfu, (1125,20))
                    print_boss(boss.hp)
                    screen.blit(block, (30,40))
                    
                    if question:

                        if q == 1: screen.blit(pygame.image.load("img/boss/test.png"), (570, 200))
                        if q == 2: screen.blit(pygame.image.load("img/boss/test2.png"), (570, 200))
                        if q == 3: screen.blit(pygame.image.load("img/boss/test3.png"), (570, 200))
                        if q == 4: screen.blit(pygame.image.load("img/boss/test4.png"), (570, 200))
                        if q == 5: screen.blit(pygame.image.load("img/boss/test5.png"), (570, 200))
                        if q == 6: screen.blit(pygame.image.load("img/boss/test6.png"), (570, 200))
                        if q == 7: screen.blit(pygame.image.load("img/boss/test7.png"), (570, 200))
                        if q == 8: screen.blit(pygame.image.load("img/boss/test8.png"), (570, 200))
                            
                    else:
                        if answ: 
                            screen.blit(goodtest,(600,200))
                        else: 
                            screen.blit(badtest,(600,200))
                    
                if boss.hp == 0:
                    test = False
                    screen.blit(pygame.image.load("img/boss/cat_end.jpg"), (0, 0))
                    endgame = True

                if player.hp<=0:
                    test=False
                    screen.blit(pygame.image.load("img/boss/death.jpg"),(0,0))
                    endgame=True

                if badend:
                    screen.blit(pygame.image.load("img/boss/badbad.jpg"), (0, 0))
                    endgame = True

                

                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                        
                    elif event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_ESCAPE:
                            Interface.menu.main_menu(screen, running)    
                                               
                        if not(test) and not(endgame):

                            if event.key == pygame.K_SPACE and not(test):
                                badend=True
                            if event.key == pygame.K_RETURN and not(badend):
                                test=True

                        if question:
                            if q == 1:
                                if event.key == pygame.K_3:
                                    boss.hp -= 1
                                    answ = True
                                elif event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_4:
                                    player.hp -= boss.damage
                                    answ = False
                                if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4:
                                    question=False
                            if q == 2:
                                if event.key == pygame.K_2:
                                    boss.hp -= 1
                                    answ = True
                                elif event.key == pygame.K_1 or event.key == pygame.K_3 or event.key == pygame.K_4:
                                    player.hp -= boss.damage
                                    answ = False
                                if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4:
                                    question = False
                            if q == 3:
                                if event.key == pygame.K_2:
                                    boss.hp -= 1
                                    answ = True
                                elif event.key == pygame.K_1 or event.key == pygame.K_3 or event.key == pygame.K_4:
                                    player.hp -= boss.damage
                                    answ = False
                                if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4:
                                    question = False
                            if q == 4:
                                if event.key == pygame.K_2:
                                    boss.hp -= 1
                                    answ = True
                                elif event.key == pygame.K_1 or event.key == pygame.K_3 or event.key == pygame.K_4:
                                    player.hp -= boss.damage
                                    answ = False
                                if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4:
                                    question = False
                            if q == 5:
                                if event.key == pygame.K_3:
                                    boss.hp -= 1
                                    answ = True
                                elif event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_4:
                                    player.hp -= boss.damage
                                    answ = False
                                if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4:
                                    question = False
                            if q == 6:
                                if event.key == pygame.K_1:
                                    boss.hp -= 1
                                    answ = True
                                elif event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4:
                                    player.hp -= boss.damage
                                    answ = False
                                if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4:
                                    question = False
                            if q == 7:
                                if event.key == pygame.K_4:
                                    boss.hp -= 1
                                    answ = True
                                elif event.key == pygame.K_1 or event.key == pygame.K_3 or event.key == pygame.K_2:
                                    player.hp -= boss.damage
                                    answ = False
                                if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4:
                                    question = False
                            if q == 8:
                                if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4:
                                    boss.hp -= 1
                                    answ = True
                                    question = False
                                                                        

                        if question == False and test and event.key == pygame.K_RETURN:
                            q += 1
                            question = True

                        if endgame and (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN):
                            mainsound.stop()      
                            Interface.game.credits(screen, running)
                        


        def credits(screen, running):
            credits = Video("video/credits.mp4")
            credits.set_size((1280, 768)) 
            flag = True
            

            while running:
                if credits.active == False:
                    Interface.menu.main_menu(screen, running)

                credits.draw(screen, (0, 0))

                Interface.print_text(screen, "Press SPACE to skip credits", 850, 0, "Grey", "fonts/SuperWebcomicBros_Rusbyyakustick_-Regular_0.ttf", 30) 

                pygame.display.update()

                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            pygame.quit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                credits.close()
                                Interface.menu.main_menu(screen, running)