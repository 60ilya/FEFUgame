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
   
        
