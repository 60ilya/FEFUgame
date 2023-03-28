import pygame
from class_files.game import Game
from class_files.classes import Player
import time



class Interface():
    def print_text(screen, message, x, y, font_color=(0, 0, 0), font_type = "", font_size = 0):
        font_type = pygame.font.Font(font_type, font_size)
        text = font_type.render(message, True, font_color)
        screen.blit(text, (x, y))

    def boss_battle(screen):
        men=pygame.image.load("img/players/boss/menu1.jpg")
        badend=pygame.image.load("img/players/boss/badbad.jpg")
        boss=pygame.image.load("img/players/boss/klunin5.png")
        test1=pygame.image.load("img/players/boss/test.png")
        test2=pygame.image.load("img/players/boss/test2.png")
        test3=pygame.image.load("img/players/boss/test3.png")
        test4=pygame.image.load("img/players/boss/test4.png")
        test5=pygame.image.load("img/players/boss/test5.png")
        test6=pygame.image.load("img/players/boss/test6.png")
        test7=pygame.image.load("img/players/boss/test7.png")
        test8=pygame.image.load("img/players/boss/test8.png")
        badtest=pygame.image.load("img/players/boss/badtest.png")
        goodtest=pygame.image.load("img/players/boss/goodtest.png")
        bigboss=pygame.image.load("img/players/boss/boss1.png")
        bigboss1=pygame.image.load("img/players/boss/boss2.png")
        bigboss2=pygame.image.load("img/players/boss/boss3.png")
        bigboss3=pygame.image.load("img/players/boss/boss5.png")
        bigboss4=pygame.image.load("img/players/boss/boss6.png")
        winner=pygame.image.load("img/players/boss/kingDima.png")
        dvfu=pygame.image.load("img/players/boss/dvfu.png")
        block=pygame.image.load("img/players/boss/block2.png")
        death=pygame.image.load("img/players/boss/death.jpg")

        square =pygame.Surface((430,65))
        square.fill("White")

        mainsound=pygame.mixer.Sound("battle_music.mp3")

        main_string1=pygame.font.Font("SuperWebcomicBros_Rusbyyakustick_-Regular_0.ttf",40)
        string2=main_string1.render("Вы готовы к бою?",False,"White")
        string3=main_string1.render("Нажмите ENTER, чтобы начать ",False,"White")
        string4=main_string1.render("Нажмите SPACE ,чтобы сбежать ",False,"White", "Black")
        main_string2=pygame.font.Font("SuperWebcomicBros_Rusbyyakustick_-Regular_0.ttf",80)
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
        bad=True
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
            
        while True:
            location=False
            screen.blit(men,(0,0))
            screen.blit(string2,(150, 360))
            screen.blit(string3,(150, 410))
            screen.blit(string4,(150, 460))
            pygame.time.delay(70)
        
            if bad == False:
                screen.blit(badend,(0,0))

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
                if p.hp==0:
                    screen.blit(death,(0,0))    
                
            if after_fight1==True:
                newfight1=False
                screen.blit(men,(0,0))
                if e.hp==200:
                    screen.blit(bigboss1,(0,100))
                elif e.hp==150:
                    screen.blit(bigboss2,(0,100))
                elif e.hp==100:
                    screen.blit(bigboss3,(0,100))
                elif e.hp==50:
                    screen.blit(bigboss4,(0,100))
                else:
                    screen.blit(bigboss,(0,100))
                    
                screen.blit(dvfu,(1125,20))
                screen.blit(square,(670,525))
                screen.blit(goodtest,(600,200))
                if e.hp==0:
                    screen.blit(cat,(0,0))
                pygame.time.delay(70)
                
            if fight2==False:
                screen.blit(men,(0,0))
                if e.hp==200:
                    screen.blit(bigboss1,(0,100))
                elif e.hp==150:
                    screen.blit(bigboss2,(0,100))
                elif e.hp==100:
                    screen.blit(bigboss3,(0,100))
                elif e.hp==50:
                    screen.blit(bigboss4,(0,100))
                else:
                    screen.blit(bigboss,(0,100))
                screen.blit(dvfu,(1125,20))
                screen.blit(test2,(570,200))
                if e.hp==0:
                    screen.blit(cat,(0,0))
                pygame.time.delay(70)

            if after_fight2==False:
                newfight2=False
                screen.blit(men,(0,0))
                if e.hp==200:
                    screen.blit(bigboss1,(0,100))
                elif e.hp==150:
                    screen.blit(bigboss2,(0,100))
                elif e.hp==100:
                    screen.blit(bigboss3,(0,100))
                elif e.hp==50:
                    screen.blit(bigboss4,(0,100))
                else:
                    screen.blit(bigboss,(0,100))
                screen.blit(dvfu,(1125,20))
                screen.blit(badtest,(600,200))
                if e.hp==0:
                    screen.blit(cat,(0,0))
                pygame.time.delay(70)
                if p.hp==0:
                    screen.blit(death,(0,0)) 
                
            if after_fight2==True:
                newfight2=False
                screen.blit(men,(0,0))
                if e.hp==200:
                    screen.blit(bigboss1,(0,100))
                elif e.hp==150:
                    screen.blit(bigboss2,(0,100))
                elif e.hp==100:
                    screen.blit(bigboss3,(0,100))
                elif e.hp==50:
                    screen.blit(bigboss4,(0,100))
                else:
                    screen.blit(bigboss,(0,100))
                screen.blit(dvfu,(1125,20))
                screen.blit(square,(670,525))
                screen.blit(goodtest,(600,200))
                if e.hp==0:
                    screen.blit(cat,(0,0))
                pygame.time.delay(70)
            
            if fight3==False:
                screen.blit(men,(0,0))
                if e.hp==200:
                    screen.blit(bigboss1,(0,100))
                elif e.hp==150:
                    screen.blit(bigboss2,(0,100))
                elif e.hp==100:
                    screen.blit(bigboss3,(0,100))
                elif e.hp==50:
                    screen.blit(bigboss4,(0,100))
                else:
                    screen.blit(bigboss,(0,100))
                screen.blit(dvfu,(1125,20))
                screen.blit(test3,(600,200))
                if e.hp==0:
                    screen.blit(cat,(0,0))
                pygame.time.delay(70)

            if after_fight3==False:
                newfight3=False
                screen.blit(men,(0,0))
                if e.hp==200:
                    screen.blit(bigboss1,(0,100))
                elif e.hp==150:
                    screen.blit(bigboss2,(0,100))
                elif e.hp==100:
                    screen.blit(bigboss3,(0,100))
                elif e.hp==50:
                    screen.blit(bigboss4,(0,100))
                else:
                    screen.blit(bigboss,(0,100))
                screen.blit(dvfu,(1125,20))
                screen.blit(badtest,(600,200))
                if e.hp==0:
                    screen.blit(cat,(0,0))
                pygame.time.delay(70)
                if p.hp==0:
                    screen.blit(death,(0,0)) 
                
            if after_fight3==True:
                newfight3=False
                screen.blit(men,(0,0))
                if e.hp==200:
                    screen.blit(bigboss1,(0,100))
                elif e.hp==150:
                    screen.blit(bigboss2,(0,100))
                elif e.hp==100:
                    screen.blit(bigboss3,(0,100))
                elif e.hp==50:
                    screen.blit(bigboss4,(0,100))
                else:
                    screen.blit(bigboss,(0,100))
                screen.blit(dvfu,(1125,20))
                screen.blit(square,(670,525))
                screen.blit(goodtest,(600,200))
                if e.hp==0:
                    screen.blit(cat,(0,0))
                pygame.time.delay(70)
            
            if fight4==False:
                screen.blit(men,(0,0))
                if e.hp==200:
                    screen.blit(bigboss1,(0,100))
                elif e.hp==150:
                    screen.blit(bigboss2,(0,100))
                elif e.hp==100:
                    screen.blit(bigboss3,(0,100))
                elif e.hp==50:
                    screen.blit(bigboss4,(0,100))
                else:
                    screen.blit(bigboss,(0,100))
                screen.blit(dvfu,(1125,20))
                screen.blit(test4,(600,200))
                if e.hp==0:
                    screen.blit(cat,(0,0))
                pygame.time.delay(70)

            if after_fight4==False:
                newfight4=False
                screen.blit(men,(0,0))
                if e.hp==200:
                    screen.blit(bigboss1,(0,100))
                elif e.hp==150:
                    screen.blit(bigboss2,(0,100))
                elif e.hp==100:
                    screen.blit(bigboss3,(0,100))
                elif e.hp==50:
                    screen.blit(bigboss4,(0,100))
                else:
                    screen.blit(bigboss,(0,100))
                screen.blit(dvfu,(1125,20))
                screen.blit(badtest,(600,200))
                if e.hp==0:
                    screen.blit(cat,(0,0))
                pygame.time.delay(70)
                if p.hp==0:
                    screen.blit(death,(0,0)) 
                
            if after_fight4==True:
                newfight4=False
                screen.blit(men,(0,0))
                if e.hp==200:
                    screen.blit(bigboss1,(0,100))
                elif e.hp==150:
                    screen.blit(bigboss2,(0,100))
                elif e.hp==100:
                    screen.blit(bigboss3,(0,100))
                elif e.hp==50:
                    screen.blit(bigboss4,(0,100))
                else:
                    screen.blit(bigboss,(0,100))
                screen.blit(dvfu,(1125,20))
                screen.blit(square,(670,525))
                screen.blit(goodtest,(600,200))
                if e.hp==0:
                    screen.blit(cat,(0,0))
                pygame.time.delay(70)

            if fight5==False:
                screen.blit(men,(0,0))
                if e.hp==200:
                    screen.blit(bigboss1,(0,100))
                elif e.hp==150:
                    screen.blit(bigboss2,(0,100))
                elif e.hp==100:
                    screen.blit(bigboss3,(0,100))
                elif e.hp==50:
                    screen.blit(bigboss4,(0,100))
                else:
                    screen.blit(bigboss,(0,100))
                screen.blit(dvfu,(1125,20))
                screen.blit(test5,(600,200))
                if e.hp==0:
                    screen.blit(cat,(0,0))
                pygame.time.delay(70)

            if after_fight5==False:
                newfight5=False
                screen.blit(men,(0,0))
                if e.hp==200:
                    screen.blit(bigboss1,(0,100))
                elif e.hp==150:
                    screen.blit(bigboss2,(0,100))
                elif e.hp==100:
                    screen.blit(bigboss3,(0,100))
                elif e.hp==50:
                    screen.blit(bigboss4,(0,100))
                else:
                    screen.blit(bigboss,(0,100))
                screen.blit(dvfu,(1125,20))
                screen.blit(badtest,(600,200))
                if e.hp==0:
                    screen.blit(cat,(0,0))
                pygame.time.delay(70)
                if p.hp==0:
                    screen.blit(death,(0,0)) 
                
            if after_fight5==True:
                newfight5=False
                screen.blit(men,(0,0))
                if e.hp==200:
                    screen.blit(bigboss1,(0,100))
                elif e.hp==150:
                    screen.blit(bigboss2,(0,100))
                elif e.hp==100:
                    screen.blit(bigboss3,(0,100))
                elif e.hp==50:
                    screen.blit(bigboss4,(0,100))
                else:
                    screen.blit(bigboss,(0,100))
                screen.blit(dvfu,(1125,20))
                screen.blit(square,(670,525))
                screen.blit(goodtest,(600,200))
                if e.hp==0:
                    screen.blit(cat,(0,0))
                pygame.time.delay(70)
                    
            if fight6==False:
                screen.blit(men,(0,0))
                if e.hp==200:
                    screen.blit(bigboss1,(0,100))
                elif e.hp==150:
                    screen.blit(bigboss2,(0,100))
                elif e.hp==100:
                    screen.blit(bigboss3,(0,100))
                elif e.hp==50:
                    screen.blit(bigboss4,(0,100))
                else:
                    screen.blit(bigboss,(0,100))
                screen.blit(dvfu,(1125,20))
                screen.blit(test6,(600,200))
                if e.hp==0:
                    screen.blit(cat,(0,0))
                pygame.time.delay(70)

            if after_fight6==False:
                newfight6=False
                screen.blit(men,(0,0))
                if e.hp==200:
                    screen.blit(bigboss1,(0,100))
                elif e.hp==150:
                    screen.blit(bigboss2,(0,100))
                elif e.hp==100:
                    screen.blit(bigboss3,(0,100))
                elif e.hp==50:
                    screen.blit(bigboss4,(0,100))
                else:
                    screen.blit(bigboss,(0,100))
                screen.blit(dvfu,(1125,20))
                screen.blit(badtest,(600,200))
                if e.hp==0:
                    screen.blit(cat,(0,0))
                pygame.time.delay(70)
                if p.hp==0:
                    screen.blit(death,(0,0)) 
                
            if after_fight6==True:
                newfight6=False
                screen.blit(men,(0,0))
                if e.hp==200:
                    screen.blit(bigboss1,(0,100))
                elif e.hp==150:
                    screen.blit(bigboss2,(0,100))
                elif e.hp==100:
                    screen.blit(bigboss3,(0,100))
                elif e.hp==50:
                    screen.blit(bigboss4,(0,100))
                else:
                    screen.blit(bigboss,(0,100))
                screen.blit(dvfu,(1125,20))
                screen.blit(square,(670,525))
                screen.blit(goodtest,(600,200))
                if e.hp==0:
                    screen.blit(cat,(0,0))
                pygame.time.delay(70)

            if fight7==False:
                screen.blit(men,(0,0))
                if e.hp==200:
                    screen.blit(bigboss1,(0,100))
                elif e.hp==150:
                    screen.blit(bigboss2,(0,100))
                elif e.hp==100:
                    screen.blit(bigboss3,(0,100))
                elif e.hp==50:
                    screen.blit(bigboss4,(0,100))
                else:
                    screen.blit(bigboss,(0,100))
                screen.blit(dvfu,(1125,20))
                screen.blit(test7,(600,200))
                if e.hp==0:
                    screen.blit(cat,(0,0))
                pygame.time.delay(70)

            if after_fight7==False:
                newfight7=False
                screen.blit(men,(0,0))
                if e.hp==200:
                    screen.blit(bigboss1,(0,100))
                elif e.hp==150:
                    screen.blit(bigboss2,(0,100))
                elif e.hp==100:
                    screen.blit(bigboss3,(0,100))
                elif e.hp==50:
                    screen.blit(bigboss4,(0,100))
                else:
                    screen.blit(bigboss,(0,100))
                screen.blit(dvfu,(1125,20))
                screen.blit(badtest,(600,200))
                if e.hp==0:
                    screen.blit(cat,(0,0))
                pygame.time.delay(70)
                if p.hp==0:
                    screen.blit(death,(0,0)) 
                
            if after_fight7==True:
                newfight7=False
                screen.blit(men,(0,0))
                if e.hp==200:
                    screen.blit(bigboss1,(0,100))
                elif e.hp==150:
                    screen.blit(bigboss2,(0,100))
                elif e.hp==100:
                    screen.blit(bigboss3,(0,100))
                elif e.hp==50:
                    screen.blit(bigboss4,(0,100))
                else:
                    screen.blit(bigboss,(0,100))
                screen.blit(dvfu,(1125,20))
                screen.blit(square,(670,525))
                screen.blit(goodtest,(600,200))
                if e.hp==0:
                    screen.blit(cat,(0,0))
                pygame.time.delay(70)

            if fight8==False:
                screen.blit(men,(0,0))
                if e.hp==200:
                    screen.blit(bigboss1,(0,100))
                elif e.hp==150:
                    screen.blit(bigboss2,(0,100))
                elif e.hp==100:
                    screen.blit(bigboss3,(0,100))
                elif e.hp==50:
                    screen.blit(bigboss4,(0,100))
                else:
                    screen.blit(bigboss,(0,100))
                screen.blit(dvfu,(1125,20))
                screen.blit(test8,(300,100))
                if e.hp==0:
                    screen.blit(cat,(0,0))
                pygame.time.delay(70)
                
            if after_fight8==True:
                newfight8=False
                screen.blit(men,(0,0))
                if e.hp==200:
                    screen.blit(bigboss1,(0,100))
                elif e.hp==150:
                    screen.blit(bigboss2,(0,100))
                elif e.hp==100:
                    screen.blit(bigboss3,(0,100))
                elif e.hp==50:
                    screen.blit(bigboss4,(0,100))
                else:
                    screen.blit(bigboss,(0,100))
                screen.blit(dvfu,(1125,20))
                screen.blit(square,(670,525))
                screen.blit(goodtest,(600,200))
                if e.hp==0:
                    screen.blit(cat,(0,0))  
                pygame.time.delay(70)
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    
                elif event.type == pygame.KEYDOWN:
                    
                    if location==False:
                        if event.key == pygame.K_SPACE:
                            bad=False
                        if event.key == pygame.K_RETURN:
                            good=False
                            
                    if fight1==False and fight2==True:
                        if event.key == pygame.K_1:
                            after_fight1=False
                            p.hp -= e.damage
                        if event.key == pygame.K_2:
                            after_fight1=False
                            p.hp -= e.damage
                        if event.key == pygame.K_3:
                            after_fight1=True
                            e.hp -= p.damage
                        if event.key == pygame.K_4:
                            after_fight1=False
                            p.hp -= e.damage
                            
                    if newfight1==False:
                        if event.key == pygame.K_RETURN:
                            fight2=False
                            
                    if fight2==False and fight3==True:
                        if event.key == pygame.K_1:
                            after_fight2=False
                            p.hp -= e.damage
                        if event.key == pygame.K_2:
                            after_fight2=True
                            e.hp -= p.damage   
                        if event.key == pygame.K_3:
                            after_fight2=False
                            p.hp -= e.damage
                        if event.key == pygame.K_4:
                            after_fight2=False
                            p.hp -= e.damage
                            
                    if newfight2==False:
                        if event.key == pygame.K_RETURN:
                            fight3=False

                    if fight3==False and fight4==True:
                        if event.key == pygame.K_1:
                            after_fight3=False
                            p.hp -= e.damage
                        if event.key == pygame.K_2:
                            after_fight3=True
                            e.hp -= p.damage   
                        if event.key == pygame.K_3:
                            after_fight3=False
                            p.hp -= e.damage
                        if event.key == pygame.K_4:
                            after_fight3=False
                            p.hp -= e.damage
                            
                    if newfight3==False:
                        if event.key == pygame.K_RETURN:
                            fight4=False

                    if fight4==False and fight5==True:
                        if event.key == pygame.K_1:
                            after_fight4=False
                            p.hp -= e.damage
                        if event.key == pygame.K_2:
                            after_fight4=True
                            e.hp -= p.damage
                        if event.key == pygame.K_3:
                            after_fight4=False
                            p.hp -= e.damage
                        if event.key == pygame.K_4:
                            after_fight4=False
                            p.hp -= e.damage

                    if newfight4==False:
                        if event.key == pygame.K_RETURN:
                            fight5=False

                    if fight5==False and fight6==True:
                        if event.key == pygame.K_1:
                            after_fight5=False
                            p.hp -= e.damage
                        if event.key == pygame.K_2:
                            after_fight5=False
                            p.hp -= e.damage
                        if event.key == pygame.K_3:
                            after_fight5=True
                            e.hp -= p.damage
                        if event.key == pygame.K_4:
                            after_fight5=False
                            p.hp -= e.damage

                    if newfight5==False:
                        if event.key == pygame.K_RETURN:
                            fight6=False

                    if fight6==False and fight7==True:
                        if event.key == pygame.K_1:
                            after_fight6=True
                            e.hp -= p.damage 
                        if event.key == pygame.K_2:
                            after_fight6=False
                            p.hp -= e.damage
                        if event.key == pygame.K_3:
                            after_fight6=False
                            p.hp -= e.damage
                        if event.key == pygame.K_4:
                            after_fight6=False
                            p.hp -= e.damage 

                    if newfight6==False:
                        if event.key == pygame.K_RETURN:
                            fight7=False

                    if fight7==False and fight8==True:
                        if event.key == pygame.K_1:
                            after_fight7=False
                            p.hp -= e.damage
                        if event.key == pygame.K_2:
                            after_fight7=False
                            p.hp -= e.damage
                        if event.key == pygame.K_3:
                            after_fight7=False
                            p.hp -= e.damage
                        if event.key == pygame.K_4:
                            after_fight7=True
                            e.hp -= p.damage 

                    if newfight7==False:
                        if event.key == pygame.K_RETURN:
                            fight8=False

                    if fight8==False and fightend==True:
                        if event.key == pygame.K_1:
                            after_fight8=True
                            e.hp -= p.damage
                        if event.key == pygame.K_2:
                            after_fight8=True
                            e.hp -= p.damage 
                        if event.key == pygame.K_3:
                            after_fight8=True
                            e.hp -= p.damage 
                        if event.key == pygame.K_4:
                            after_fight8=True
                            e.hp -= p.damage 

                    if newfight8==False:
                        if event.key == pygame.K_RETURN:
                            fight8=False
                    
        
            pygame.display.update()
   
        


    class minimap():
        def room_minimap(map, room):
            # pygame.draw.rect(room, "Grey", (1075, 15, 200, 200))

            for i in range(10):
                for j in range(10):
                    if map[i][j] in range(1, 3):
                        pygame.draw.rect(room, "Black", (1075 + (j + 1) * 20, 15 + (i + 1) * 20, 17, 17))

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

            if player.x < 226 and map[room_x][room_y - 1] in range(1, 3):
                map[room_x][room_y] = 1
                map[room_x][room_y - 1] = 2
                room_y -= 1
                img = Game.map.room_choose(map, room_x, room_y)
                room = pygame.image.load(img)
                player.x = 965
                player.y = 408
                Interface.minimap.player_minimap(map, room)


            if player.x > 1000 and map[room_x][room_y + 1] in range(1, 3):
                map[room_x][room_y] = 1
                map[room_x][room_y + 1] = 2
                room_y += 1
                img = Game.map.room_choose(map, room_x, room_y)
                room = pygame.image.load(img)
                player.x = 258
                player.y = 418
                Interface.minimap.player_minimap(map, room)

            if player.y < 195 and map[room_x - 1][room_y] in range(1, 3):
                map[room_x][room_y] = 1
                map[room_x - 1][room_y] = 2
                room_x -= 1
                img = Game.map.room_choose(map, room_x, room_y)
                room = pygame.image.load(img)
                player.x = 611
                player.y = 603
                Interface.minimap.player_minimap(map, room)


            if player.y > 640 and map[room_x + 1][room_y] in range(1, 3):
                map[room_x][room_y] = 1
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
            on = pygame.image.load("img/sound/on.png")
            off = pygame.image.load("img/sound/off.png")

            menu = pygame.image.load("img/menu/main_menu.jpg")
            vanechka = pygame.image.load("img/players/big/vanechka.png")
            shaman = pygame.image.load("img/players/big/shaman.png")
            dimochka = pygame.image.load("img/players/big/dimochka.png")

            dimochka_small = pygame.image.load("img/players/dimochka.png")
            vanechka_small = pygame.image.load("img/players/vanechka.png")
            shaman_small = pygame.image.load("img/players/shaman.png")



            flPause = False

            choose = 1

            while running:
                screen.blit(menu, (0, 0))

                if not flPause:
                    screen.blit(on, (10, 10))
                else:
                    screen.blit(off, (10, 10))

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
                            flPause = not flPause
                            if flPause:
                                pygame.mixer.music.pause()
                            else:
                                pygame.mixer.music.unpause()
                        if event.key == pygame.K_LEFT:
                            if choose == 1:
                                choose = 0
                            elif choose == 2:
                                choose = 1
                            else:
                                choose = 2
                        if event.key == pygame.K_RIGHT:
                            if choose == 1:
                                choose = 2
                            elif choose == 2:
                                choose = 0
                            else:
                                choose = 1   

                        if event.key == pygame.K_SPACE:
                            print(choose)
                            if choose == 0:
                                Interface.game.main_game(screen, vanechka_small, 2, 4)
                            elif choose == 1:
                                Interface.game.main_game(screen, dimochka_small, 3, 3)
                            else:
                                Interface.game.main_game(screen, shaman_small, 4, 2)

                pygame.display.update()



        def main_menu(screen, running):
            on = pygame.image.load("img/sound/on.png")
            off = pygame.image.load("img/sound/off.png")

            pygame.mixer.music.load("music/main.mp3")
            pygame.mixer.music.play(-1)
            FPS = 15
            direct_y = 1
            clock = pygame.time.Clock()

            menu = pygame.image.load("img/menu/main_menu.jpg")
            y = 540
            flPause = 0

            while running:
                clock.tick(FPS)
                screen.blit(menu, (0, 0))
                
                if not flPause:
                    screen.blit(on, (10, 10))
                else:
                    screen.blit(off, (10, 10))

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
                            flPause = not flPause
                            if flPause:
                                pygame.mixer.music.pause()
                            else:
                                pygame.mixer.music.unpause()
                        if event.key == pygame.K_SPACE:
                            Interface.menu.player_choose(screen, running)


                

    class game():
        def main_game(screen, texture, hp, damage):
            room_x = 4
            room_y = 4
            running = True
            # player_texture = pygame.image.load("img/players/dimochka.png")

            player = Player(texture, None, hp, damage, 0.6, 0.4, None, 540, 300)
            player.hitbox = texture.get_rect(topleft = (player.x, player.y))

            map = Game.map.rand_map()
            room = pygame.image.load(Game.map.room_choose(map, room_x, room_y))

            while running:

                
                Interface.minimap.room_minimap(map, room)
                Interface.minimap.player_minimap(map, room)

                room, room_x, room_y = Interface.room.room_changing(player, map, room_x, room_y, room)

                screen.blit(room, (0, 0))

                screen.blit(player.texture, (player.x, player.y))
                Player.moving(player)

                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()

    
        
