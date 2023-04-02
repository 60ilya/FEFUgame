import pygame
import math
import random

#основной класс
class Character():
    def __init__(self, texture, hitbox, hp, damage, speed, diagonal_speed, x, y, item):
        self.texture = texture
        self.hitbox = hitbox
        self.hp = hp
        self.damage = damage
        self.speed = speed
        self.diagonal_speed = diagonal_speed
        self.x = x
        self.y = y
        self.item = item
#класс игрока
class Player(Character):
    def __init__(self, texture, hitbox, hp, damage, speed, diagonal_speed, shield, x, y, item):
        super().__init__(texture, hitbox, hp, damage, speed, diagonal_speed, x, y, item)
        self.shield = shield
        
    #функция использования предмета
    def use_item(self, item):
        if isinstance(item, HealthPotion):
            self.hp += item.heal_amount
        elif isinstance(item, SpeedBoost):
            self.speed += item.duration
        elif isinstance(item, DamageBoost):
            self.damage += item.duration

    def room_coordinates(self, map):
        for y in range(10):
            for x in range(10):
                if map[x][y] == 2:
                    xy = [x, y]
                    return xy

    #функция для передвижения персонажа
    def moving(self):
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and keys[pygame.K_a]:

            if not(self.x > 244 and self.x < 972):
                if (self.y > 377 and self.y < 447): #ширина двери
                    self.y -= self.diagonal_speed
            elif self.y > 223 or (self.x > 570 and self.x < 650):
                self.y -= self.diagonal_speed

            if not(self.y > 222 and self.y < 614):
                if (self.x > 570 and self.x < 646): #ширина двери
                    self.x -= self.diagonal_speed
            elif self.x > 250 or (self.y > 377 and self.y < 447):
                self.x -= self.diagonal_speed

        elif keys[pygame.K_a] and keys[pygame.K_s]:

            if not(self.y > 222 and self.y < 614):
                if (self.x > 570 and self.x < 646): #ширина двери
                    self.x -= self.diagonal_speed
            elif self.x > 250 or (self.y > 377 and self.y < 447):
                self.x -= self.diagonal_speed

            if not(self.x > 244 and self.x < 972):
                if (self.y > 377 and self.y < 447): #ширина двери
                    self.y += self.diagonal_speed
            elif self.y < 610 or (self.x > 570 and self.x < 650):
                self.y += self.diagonal_speed

        elif keys[pygame.K_s] and keys[pygame.K_d]:
            if not(self.x > 244 and self.x < 972):
                if (self.y > 377 and self.y < 447): #ширина двери
                    self.y += self.diagonal_speed
            elif self.y < 610 or (self.x > 570 and self.x < 650):
                self.y += self.diagonal_speed

            if not(self.y > 222 and self.y < 614):
                if (self.x > 565 and self.x < 645): #ширина двери
                    self.x += self.diagonal_speed
            elif self.x < 970 or (self.y > 377 and self.y < 447):
                self.x += self.diagonal_speed
                
        elif keys[pygame.K_d] and keys[pygame.K_w]:

            if not(self.y > 222 and self.y < 614):
                if (self.x > 565 and self.x < 645): #ширина двери
                    self.x += self.diagonal_speed
            elif self.x < 970 or (self.y > 377 and self.y < 447):
                self.x += self.diagonal_speed

            if not(self.x > 244 and self.x < 972):
                if (self.y > 377 and self.y < 447): #ширина двери
                    self.y -= self.diagonal_speed
            elif self.y > 223 or (self.x > 570 and self.x < 650):
                self.y -= self.diagonal_speed

        elif keys[pygame.K_a]:

            if not(self.y > 222 and self.y < 614):
                if (self.x > 570 and self.x < 646): #ширина двери
                    self.x -= self.speed
            elif self.x > 250 or (self.y > 377 and self.y < 447):
                self.x -= self.speed

        elif keys[pygame.K_d]:

            if not(self.y > 222 and self.y < 614):
                if (self.x > 565 and self.x < 645): #ширина двери
                    self.x += self.speed
            elif self.x < 970 or (self.y > 377 and self.y < 447):
                self.x += self.speed

        elif keys[pygame.K_s]:

            if not(self.x > 244 and self.x < 972):
                if (self.y > 377 and self.y < 447): #ширина двери
                    self.y += self.speed
            elif self.y < 610 or (self.x > 570 and self.x < 650):
                self.y += self.speed

        elif keys[pygame.K_w]:
            if not(self.x > 244 and self.x < 972):
                if (self.y > 377 and self.y < 447): #ширина двери
                    self.y -= self.speed
            elif self.y > 223 or (self.x > 570 and self.x < 650):
                self.y -= self.speed



#класс врагов
class Enemy(Character):
    def __init__(self, hp, damage, texture, speed, x, y):
        super().__init__(hp, damage, texture, speed, x, y)

#класс воина
class Warrior(Player):
    def __init__(self, texture, hitbox, hp, damage, speed, diagonal_speed, shield, x, y, item):
        super().__init__(texture, hitbox, hp, damage, speed, diagonal_speed, shield, x, y, item)



#класс лучника
class Archer(Player):
    def __init__(self, texture, hitbox, hp, damage, speed, diagonal_speed, shield, x, y, item):
        super().__init__(texture, hitbox, hp, damage, speed, diagonal_speed, shield, x, y, item)


    def shooting(self, bullets, screen, egg):
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
            bullet.draw(screen, egg)
            
    



class Mob():
    image = pygame.image.load("img/enemy/mobs/cats.png")
    
    def __init__(self, hp, damage, texture, speed, x, y, hitbox):
        self.hp = hp
        self.damage = damage
        self.texture = texture
        self.speed = speed
        self.x = x
        self.y = y
        self.hitbox = hitbox


    def collision(player, mobs_list, bullets: list):
        if len(mobs_list) > 0 and len(bullets) > 0:
            for bullet in bullets:
                print(bullet.hitbox)
                for mob in mobs_list:
                    if bullet.hitbox.colliderect(mob.hitbox):
                        print("collision")
                        if len(bullets) != 0:
                            bullets.pop(bullets.index(bullet))
                        mobs_list.pop(mobs_list.index(mob))
                        print(mobs_list)
                    
        
        return mobs_list
    
    def get_hitbox(mobs_list):
        for mob in mobs_list:
            mob.hitbox = mob.texture.get_rect(topleft=(mob.x, mob.y))

    def spawn(map, screen, xy, mobs_room, mob1, mob2, mob3, mob4, mobs_list):
        
        if xy in mobs_room:

            if mob1 in mobs_list:
                screen.blit(mob1.texture, (mob1.x, mob1.y))
            if mob2 in mobs_list:
                screen.blit(mob2.texture, (mob2.x, mob2.y))
            if mob3 in mobs_list:
                screen.blit(mob3.texture, (mob3.x, mob3.y))
            if mob4 in mobs_list:
                screen.blit(mob4.texture, (mob4.x, mob4.y))

            if len(mobs_list) == 0:
                mobs_room.remove(xy)
                print("REMOVE")

    def move_towards_player(mobs_list, player):
        for mob in mobs_list:
            dx, dy = player.x - mob.x, player.y - mob.y
            dist = math.hypot(dx, dy)
            dx, dy = dx / dist, dy / dist  # Normalize.
            # Move along this normalized vector towards the player at current speed.
            mob.x += dx * mob.speed
            mob.y += dy * mob.speed
            print(mob.hitbox)

#класс босса
class Boss:
    def __init__(self, texture, hp, damage, x, y):
        self.texture = texture
        self.hp = hp
        self.damage = damage
        self.x = x
        self.y = y
        self.alive = True    

    def spawn(map, screen, xy, mobs_room, mob1, mob2, mob3, mob4, mobs_list):
        if xy in mobs_room:
            if mob1 in mobs_list:
                screen.blit(mob1.texture, (mob1.x, mob1.y))
            if mob2 in mobs_list:
                screen.blit(mob2.texture, (mob2.x, mob2.y))
            if mob3 in mobs_list:
                screen.blit(mob3.texture, (mob3.x, mob3.y))
            if mob4 in mobs_list:
                screen.blit(mob4.texture, (mob4.x, mob4.y))
            if len(mobs_room) == 0:
                mobs_room.remove(xy)
                    # return mob1, mob2, mob3, mob4



#класс стрелы
class Arrow:
    image = pygame.image.load("img/shoot/egg.png")

    def __init__(self, x, y, facing, texture):
        self.x = x
        self.y = y
        self.facing = facing
        self.vel = 3
        self.hitbox = Arrow.image.get_rect(topleft = (self.x, self.y))
        self.texture = texture

    def draw(self, screen, egg):
        screen.blit(egg, (self.x, self.y))

    def get_hitbox(bullets):
        for bullet in bullets:
            bullet.hitbox = bullet.texture.get_rect(topleft=(bullet.x, bullet.y))


class Item:
    def __init__(self, texture):
        self.texture = texture
     #фунцкия создания предметов   
    def create_item(gold_x, gold_y, map, item, screen, player):
        if player.shield == False:
            if map[gold_x][gold_y] == 2:
                screen.blit(item, (570, 400))
    #функция использования
    def collision(item_hitbox, player, gold_x, gold_y, map, item):
        if player.hitbox.colliderect(item_hitbox):
            if map[gold_x][gold_y] == 2:
                item.use(player)
                player.shield = True
                gold_x, gold_y = 9, 9




#класс хилки
class HealthPotion(Item):
    def __init__(self, texture):
        super().__init__(texture)
        self.heal_amount = 1
    #функ создания предмета
    def create_item(gold_x, gold_y, map, item, screen):
        if map[gold_x][gold_y] == 2:
            screen.blit(item, (570, 400))
    #функ использования
    def use(self, player):
        if player.item == False:
            player.item = True
            player.hp += 1

#класс буста на скорость 
class SpeedBoost(Item):
    def __init__(self, texture):
        super().__init__(texture)
        self.duration = 0.5
    #функ создания предмета
    def create_item(gold_x, gold_y, map, item, screen):
        if map[gold_x][gold_y] == 2:
            screen.blit(item, (570, 400))
    #функ использования
    def use(self, player):
        if player.item == False:
            player.item = True
            player.speed += 0.5

#класс буста силы
class DamageBoost(Item):
    def __init__(self, texture):
        super().__init__(texture)
        self.duration = 2
    #функ создания предмета
    def create_item(gold_x, gold_y, map, item, screen):
        if map[gold_x][gold_y] == 2:
            screen.blit(item, (570, 400))
    #функ использования
    def use(self, player):
        if player.item == False:
            player.item = True  
            player.damage += 2
