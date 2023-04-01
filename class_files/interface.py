import pygame
from pyvidplayer import Video
from class_files.game import Game
from class_files.classes import Player, SpeedBoost, HealthPotion, DamageBoost, Item, Archer, Warrior, Arrow, Boss
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
                for i in range(10):
                    print(map[i])

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
                for i in range(10):
                    print(map[i])

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
                for i in range(10):
                    print(map[i])

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
                            Interface.game.main_game(screen, choose, running)

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
        def main_game(screen, choose, running):
            room_x = 4
            room_y = 4
            running = True
            
            if choose == 0:
                vanechka_small = pygame.image.load("img/players/vanechka.png")
                player = Warrior(vanechka_small, None, 2, 4, 1.5, 1.2, False, 540, 300, False)            
            elif choose == 1:
                dimochka_small = pygame.image.load("img/players/dimochka.png")
                player = Warrior(dimochka_small, None, 3, 3, 1.5, 1.2, False, 540, 300, False) 
            else:
                shaman_small = pygame.image.load("img/players/shaman.png")
                player = Archer(shaman_small, None, 4, 2, 1.5, 1.2, False, 540, 300, False)

            

            map = Game.map.rand_map()
            room = pygame.image.load(Game.map.room_choose(map, room_x, room_y))

            gold_x, gold_y, item = Interface.room.init_treasure_room(map, screen)
            item_hitbox = item.texture.get_rect(topleft = (570, 400))

            bullets = []
            


            while running:
                player.hitbox = player.texture.get_rect(topleft = (player.x, player.y))

                Game.map.room_inv_block(map, room_x, room_y, player)
                
                Interface.minimap.room_minimap(map, room)
                Interface.minimap.player_minimap(map, room)

                room, room_x, room_y = Interface.room.room_changing(player, map, room_x, room_y, room)

                screen.blit(room, (0, 0))

                screen.blit(player.texture, (player.x, player.y))
                Player.moving(player)
                
                Interface.print_stat(screen, player)

                Item.create_item(gold_x, gold_y, map, item.texture, screen, player)
                Item.collision(item_hitbox, player, gold_x, gold_y, map, item)
                
                for bullet in bullets:
                    if bullet.x > 230 and bullet.x < 1100 and bullet.y > 222 and bullet.y < 650:
                        if bullet.facing == "a":
                            bullet.x -= bullet.vel
                        if bullet.facing == "d":
                            bullet.x += bullet.vel
                        if bullet.facing == "w":
                            bullet.y -= bullet.vel
                        if bullet.facing == "s":
                            bullet.y += bullet.vel 
                         
                    else:
                        bullets.pop(bullets.index(bullet))

                for bullet in bullets:
                    bullet.draw(screen)

                
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
                            Interface.game.main_game(screen, choose, running)

                        if event.key == pygame.K_b: #временное включение босса
                            Interface.game.boss_fight(screen, player, running)
                        
                        if event.key == pygame.K_ESCAPE:
                            Interface.menu.main_menu(screen, running)
                        
                        if event.key == pygame.K_LEFT:
                            if len(bullets) < 5:
                                bullets.append(Arrow(player.x + 35, player.y + 35, 10, "Red", "a"))

                        if event.key == pygame.K_RIGHT:
                            if len(bullets) < 5:
                                bullets.append(Arrow(player.x + 35, player.y + 35, 10, "Red", "d"))
                            
                        if event.key == pygame.K_UP:
                            if len(bullets) < 5:
                                bullets.append(Arrow(player.x + 35, player.y + 35, 10, "Red", "w"))
                                
                        if event.key == pygame.K_DOWN:
                            if len(bullets) < 5:
                                bullets.append(Arrow(player.x + 35, player.y + 35, 10, "Red", "s"))

        def boss_fight(screen, player, running):
            
            boss = Boss(pygame.image.load("img/boss/klunin5.png"), 5, 1, 500, 100)

            # if player_rect.colliderect(klenin_rect):
            #         location=False
            #         screen.blit(men,(0,0))
            #         screen.blit(string2,(150, 360))
            #         screen.blit(string3,(150, 410))
            #         screen.blit(string4,(150, 460))
            #         pygame.time.delay(70)

            def print_boss(hp):
                if hp==4:
                    screen.blit(bigboss1,(0,100))
                elif hp==3:
                    screen.blit(bigboss2,(0,100))
                elif hp==2:
                    screen.blit(bigboss3,(0,100))
                elif hp==1:
                    screen.blit(bigboss4,(0,100))
                else:
                    screen.blit(bigboss,(0,100))
                print(hp)

            pygame.init()
            screen=pygame.display.set_mode((1280, 768))

            bg=pygame.image.load("img/boss/bossroom.jpg")
            men=pygame.image.load("img/boss/menu1.jpg")
            cat=pygame.image.load("img/boss/cat_end.jpg")
            finalmap=pygame.image.load("img/boss/map2.jpg")
            badend=pygame.image.load("img/boss/badbad.jpg")
            test1=pygame.image.load("img/boss/test.png")
            test2=pygame.image.load("img/boss/test2.png")
            test3=pygame.image.load("img/boss/test3.png")
            test4=pygame.image.load("img/boss/test4.png")
            test5=pygame.image.load("img/boss/test5.png")
            test6=pygame.image.load("img/boss/test6.png")
            test7=pygame.image.load("img/boss/test7.png")
            test8=pygame.image.load("img/boss/test8.png")
            badtest=pygame.image.load("img/boss/badtest.png")
            goodtest=pygame.image.load("img/boss/goodtest.png")
            bigboss=pygame.image.load("img/boss/boss1.png")
            bigboss1=pygame.image.load("img/boss/boss2.png")
            bigboss2=pygame.image.load("img/boss/boss3.png")
            bigboss3=pygame.image.load("img/boss/boss5.png")
            bigboss4=pygame.image.load("img/boss/boss6.png")
            winner=pygame.image.load("img/boss/kingDima.png")
            dvfu=pygame.image.load("img/boss/dvfu.png")
            block=pygame.image.load("img/boss/block2.png")
            death=pygame.image.load("img/boss/death.jpg")

            square = pygame.Surface((430,65))
            square.fill("White")

            mainsound=pygame.mixer.Sound("music/battle_music.mp3")

            main_string1=pygame.font.Font("fonts/SuperWebcomicBros_Rusbyyakustick_-Regular_0.ttf",40)
            string2=main_string1.render("Вы готовы к бою?",False,"White")
            string3=main_string1.render("Нажмите ENTER, чтобы начать ",False,"White")
            string4=main_string1.render("Нажмите SPACE ,чтобы сбежать ",False,"White", "Black")
            main_string2=pygame.font.Font("fonts/SuperWebcomicBros_Rusbyyakustick_-Regular_0.ttf",80)
            string5=main_string2.render("Winner",False,"Gold")

            newfight1=True
            newfight2=True
            newfight3=True
            newfight4=True
            newfight5=True
            newfight6=True
            newfight7=True
            newfight8=True

            fight2=True
            fight3=True
            fight4=True
            fight5=True
            fight6=True
            fight7=True
            fight8=True
            fightend=True

            good=True
            bad=False
            loose=False
            victory=True
            location=True
            fight1=True

            after_fight1=2
            after_fight2=2
            after_fight3=2
            after_fight4=2
            after_fight5=2
            after_fight6=2
            after_fight7=2
            after_fight8=2
            
            test=False
            answ=True

            while True:
                mainsound.play()
                screen.blit(bg,(0,0))
                screen.blit(boss.texture,(boss.x, boss.y))
                screen.blit(player.texture ,(player.x, player.y))
                        



                location=False 
                screen.blit(men,(0,0))
                screen.blit(string2,(150, 360))
                screen.blit(string3,(150, 410))
                screen.blit(string4,(150, 460))
                pygame.time.delay(70)

                if test:
                    screen.blit(men,(0,0))
                    screen.blit(dvfu,(1125,20))
                    screen.blit(bigboss,(0,100))
                    if answ:
                        screen.blit(goodtest,(600,200))
                    else:
                        screen.blit(badtest,(600,200))

                if good == False:
                    fight1=False
                    screen.blit(men,(0,0))
                    screen.blit(bigboss,(0,100))
                    screen.blit(test1,(600,200))
                    screen.blit(dvfu,(1125,20))
                    screen.blit(block,(30,40))
                    pygame.time.delay(70)
                    
                if after_fight1==False:
                    newfight1=False
                    screen.blit(men,(0,0))
                    screen.blit(dvfu,(1125,20))
                    screen.blit(bigboss,(0,100))
                    screen.blit(badtest,(600,200))
                    pygame.time.delay(70)
                    if player.hp==0:
                        screen.blit(death,(0,0))    
                    
                if after_fight1==True:
                    newfight1=False
                    screen.blit(men,(0,0))
                    print_boss(boss.hp)
                        
                    screen.blit(dvfu,(1125,20))
                    screen.blit(square,(670,525))
                    screen.blit(goodtest,(600,200))

                    pygame.time.delay(70)
                    
                if fight2==False:
                    screen.blit(men,(0,0))
                    print_boss(boss.hp)
                    screen.blit(dvfu,(1125,20))
                    screen.blit(test2,(570,200))

                    pygame.time.delay(70)

                if after_fight2==False:
                    newfight2=False
                    screen.blit(men,(0,0))
                    print_boss(boss.hp)
                    screen.blit(dvfu,(1125,20))
                    screen.blit(badtest,(600,200))

                    pygame.time.delay(70)
                    if player.hp==0:
                        screen.blit(death,(0,0)) 
                    
                if after_fight2==True:
                    newfight2=False
                    screen.blit(men,(0,0))
                    print_boss(boss.hp)
                    screen.blit(dvfu,(1125,20))
                    screen.blit(square,(670,525))
                    screen.blit(goodtest,(600,200))

                    pygame.time.delay(70)
                
                if fight3==False:
                    screen.blit(men,(0,0))
                    print_boss(boss.hp)
                    screen.blit(dvfu,(1125,20))
                    screen.blit(test3,(600,200))
                    if boss.hp==0:
                        screen.blit(cat,(0,0))
                    pygame.time.delay(70)

                if after_fight3==False:
                    newfight3=False
                    screen.blit(men,(0,0))
                    print_boss(boss.hp)
                    screen.blit(dvfu,(1125,20))
                    screen.blit(badtest,(600,200))
                    if boss.hp==0:
                        screen.blit(cat,(0,0))
                    pygame.time.delay(70)
                    if player.hp==0:
                        screen.blit(death,(0,0)) 
                    
                if after_fight3==True:
                    newfight3=False
                    screen.blit(men,(0,0))
                    print_boss(boss.hp)
                    screen.blit(dvfu,(1125,20))
                    screen.blit(square,(670,525))
                    screen.blit(goodtest,(600,200))
                    if boss.hp==0:
                        screen.blit(cat,(0,0))
                    pygame.time.delay(70)
                
                if fight4==False:
                    screen.blit(men,(0,0))
                    print_boss(boss.hp)
                    screen.blit(dvfu,(1125,20))
                    screen.blit(test4,(600,200))

                    pygame.time.delay(70)

                if after_fight4==False:
                    newfight4=False
                    screen.blit(men,(0,0))
                    print_boss(boss.hp)
                    screen.blit(dvfu,(1125,20))
                    screen.blit(badtest,(600,200))

                    pygame.time.delay(70)
                    if player.hp==0:
                        screen.blit(death,(0,0)) 
                    
                if after_fight4==True:
                    newfight4=False
                    screen.blit(men,(0,0))
                    print_boss(boss.hp)
                    screen.blit(dvfu,(1125,20))
                    screen.blit(square,(670,525))
                    screen.blit(goodtest,(600,200))

                    pygame.time.delay(70)

                if fight5==False:
                    screen.blit(men,(0,0))
                    print_boss(boss.hp)
                    screen.blit(dvfu,(1125,20))
                    screen.blit(test5,(600,200))

                    pygame.time.delay(70)

                if after_fight5==False:
                    newfight5=False
                    screen.blit(men,(0,0))
                    print_boss(boss.hp)
                    screen.blit(dvfu,(1125,20))
                    screen.blit(badtest,(600,200))

                    pygame.time.delay(70)
                    if player.hp==0:
                        screen.blit(death,(0,0)) 
                    
                if after_fight5==True:
                    newfight5=False
                    screen.blit(men,(0,0))
                    print_boss(boss.hp)
                    screen.blit(dvfu,(1125,20))
                    screen.blit(square,(670,525))
                    screen.blit(goodtest,(600,200))

                    pygame.time.delay(70)
                        
                if fight6==False:
                    screen.blit(men,(0,0))
                    print_boss(boss.hp)
                    screen.blit(dvfu,(1125,20))
                    screen.blit(test6,(600,200))

                    pygame.time.delay(70)

                if after_fight6==False:
                    newfight6=False
                    screen.blit(men,(0,0))
                    print_boss(boss.hp)
                    screen.blit(dvfu,(1125,20))
                    screen.blit(badtest,(600,200))

                    pygame.time.delay(70)
                    if player.hp==0:
                        screen.blit(death,(0,0)) 
                    
                if after_fight6==True:
                    newfight6=False
                    screen.blit(men,(0,0))
                    print_boss(boss.hp)
                    screen.blit(dvfu,(1125,20))
                    screen.blit(square,(670,525))
                    screen.blit(goodtest,(600,200))

                    pygame.time.delay(70)

                if fight7==False:
                    screen.blit(men,(0,0))
                    print_boss(boss.hp)
                    screen.blit(dvfu,(1125,20))
                    screen.blit(test7,(600,200))

                    pygame.time.delay(70)

                if after_fight7==False:
                    newfight7=False
                    screen.blit(men,(0,0))
                    print_boss(boss.hp)
                    screen.blit(dvfu,(1125,20))
                    screen.blit(badtest,(600,200))

                    pygame.time.delay(70)
                    if player.hp==0:
                        screen.blit(death,(0,0)) 
                    
                if after_fight7==True:
                    newfight7=False
                    screen.blit(men,(0,0))
                    print_boss(boss.hp)
                    screen.blit(dvfu,(1125,20))
                    screen.blit(square,(670,525))
                    screen.blit(goodtest,(600,200))

                    pygame.time.delay(70)

                if fight8==False:
                    screen.blit(men,(0,0))
                    print_boss(boss.hp)
                    screen.blit(dvfu,(1125,20))
                    screen.blit(test8,(300,100))
                    pygame.time.delay(70)
                    
                if after_fight8==True:
                    newfight8=False
                    screen.blit(men,(0,0))
                    print_boss(boss.hp)
                    screen.blit(dvfu,(1125,20))
                    screen.blit(square,(670,525))
                    screen.blit(goodtest,(600,200)) 
                    pygame.time.delay(70)

                if boss.hp==0:
                    screen.blit(cat,(0,0))

                if player.hp==0:
                    screen.blit(death,(0,0))

                if bad:
                    screen.blit(badend,(0,0))
                    loose=True

                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                        
                    elif event.type == pygame.KEYDOWN:
                        
                        if location==False:
                            if event.key == pygame.K_SPACE and good:
                                bad=True
                            if event.key == pygame.K_RETURN and not(bad):
                                good=False
                                                       
                        # if fight1==False and fight2==True:
                        #     if event.key == pygame.K_1:
                        #         after_fight1=False
                        #         player.hp -= boss.damage
                        #     if event.key == pygame.K_2:
                        #         after_fight1=False
                        #         player.hp -= boss.damage
                        #     if event.key == pygame.K_3:
                        #         after_fight1=True
                        #         boss.hp -= 1
                        #     if event.key == pygame.K_4:
                        #         after_fight1=False
                        #         player.hp -= boss.damage

                        if fight1==False and fight2==True:
                            if event.key == pygame.K_1:
                                after_fight1=False
                                player.hp -= boss.damage
                            if event.key == pygame.K_2:
                                after_fight1=False
                                player.hp -= boss.damage
                            if event.key == pygame.K_3:
                                after_fight1=True
                                boss.hp -= 1
                            if event.key == pygame.K_4:
                                after_fight1=False
                                player.hp -= boss.damage
                                
                        if newfight1==False:
                            if event.key == pygame.K_RETURN:
                                fight2=False
                                
                        if fight2==False and fight3==True:
                            if event.key == pygame.K_1:
                                after_fight2=False
                                player.hp -= boss.damage
                            if event.key == pygame.K_2:
                                after_fight2=True
                                boss.hp -= 1   
                            if event.key == pygame.K_3:
                                after_fight2=False
                                player.hp -= boss.damage
                            if event.key == pygame.K_4:
                                after_fight2=False
                                player.hp -= boss.damage
                                
                        if newfight2==False:
                            if event.key == pygame.K_RETURN:
                                fight3=False

                        if fight3==False and fight4==True:
                            if event.key == pygame.K_1:
                                after_fight3=False
                                player.hp -= boss.damage
                            if event.key == pygame.K_2:
                                after_fight3=True
                                boss.hp -= 1   
                            if event.key == pygame.K_3:
                                after_fight3=False
                                player.hp -= boss.damage
                            if event.key == pygame.K_4:
                                after_fight3=False
                                player.hp -= boss.damage
                                
                        if newfight3==False:
                            if event.key == pygame.K_RETURN:
                                fight4=False

                        if fight4==False and fight5==True:
                            if event.key == pygame.K_1:
                                after_fight4=False
                                player.hp -= boss.damage
                            if event.key == pygame.K_2:
                                after_fight4=True
                                boss.hp -= 1
                            if event.key == pygame.K_3:
                                after_fight4=False
                                player.hp -= boss.damage
                            if event.key == pygame.K_4:
                                after_fight4=False
                                player.hp -= boss.damage

                        if newfight4==False:
                            if event.key == pygame.K_RETURN:
                                fight5=False

                        if fight5==False and fight6==True:
                            if event.key == pygame.K_1:
                                after_fight5=False
                                player.hp -= boss.damage
                            if event.key == pygame.K_2:
                                after_fight5=False
                                player.hp -= boss.damage
                            if event.key == pygame.K_3:
                                after_fight5=True
                                boss.hp -= 1
                            if event.key == pygame.K_4:
                                after_fight5=False
                                player.hp -= boss.damage

                        if newfight5==False:
                            if event.key == pygame.K_RETURN:
                                fight6=False

                        if fight6==False and fight7==True:
                            if event.key == pygame.K_1:
                                after_fight6=True
                                boss.hp -= 1 
                            if event.key == pygame.K_2:
                                after_fight6=False
                                player.hp -= boss.damage
                            if event.key == pygame.K_3:
                                after_fight6=False
                                player.hp -= boss.damage
                            if event.key == pygame.K_4:
                                after_fight6=False
                                player.hp -= boss.damage 

                        if newfight6==False:
                            if event.key == pygame.K_RETURN:
                                fight7=False

                        if fight7==False and fight8==True:
                            if event.key == pygame.K_1:
                                after_fight7=False
                                player.hp -= boss.damage
                            if event.key == pygame.K_2:
                                after_fight7=False
                                player.hp -= boss.damage
                            if event.key == pygame.K_3:
                                after_fight7=False
                                player.hp -= boss.damage
                            if event.key == pygame.K_4:
                                after_fight7=True
                                boss.hp -= 1 

                        if newfight7==False:
                            if event.key == pygame.K_RETURN:
                                fight8=False

                        if fight8==False and fightend==True:
                            if event.key == pygame.K_1:
                                after_fight8=True
                                boss.hp -= 1
                            if event.key == pygame.K_2:
                                after_fight8=True
                                boss.hp -= 1 
                            if event.key == pygame.K_3:
                                after_fight8=True
                                boss.hp -= 1 
                            if event.key == pygame.K_4:
                                after_fight8=True
                                boss.hp -= 1 

                        if newfight8==False:
                            if event.key == pygame.K_RETURN:
                                fight8=False  

                        if ((bad and loose) or boss.hp==0) and (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN):
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

                Interface.print_text(screen, "Press SPACE to skip credits", 900, 0, "Grey", "fonts/SuperWebcomicBros_Rusbyyakustick_-Regular_0.ttf", 30) 
                

                pygame.display.update()

                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            pygame.quit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                credits.close()
                                Interface.menu.main_menu(screen, running)


