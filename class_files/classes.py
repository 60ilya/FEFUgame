import pygame
import random

class Character:
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
        
class Player(Character):
    def __init__(self, texture, hitbox, hp, damage, speed, diagonal_speed, shield, x, y, item):
        super().__init__(texture, hitbox, hp, damage, speed, diagonal_speed, x, y, item)
        self.shield = shield
        

    def use_item(self, item):
        if isinstance(item, HealthPotion):
            self.hp += item.heal_amount
        elif isinstance(item, SpeedBoost):
            self.speed += item.duration
        elif isinstance(item, DamageBoost):
            self.damage += item.duration

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



class Enemy(Character):
    def __init__(self, hp, damage, texture, speed, x, y):
        super().__init__(hp, damage, texture, speed, x, y)


class Warrior(Player):
    def __init__(self, texture, hitbox, hp, damage, speed, diagonal_speed, shield, x, y, item):
        super().__init__(texture, hitbox, hp, damage, speed, diagonal_speed, shield, x, y, item)




class Archer(Player):
    def __init__(self, texture, hitbox, hp, damage, speed, diagonal_speed, shield, x, y, item):
        super().__init__(texture, hitbox, hp, damage, speed, diagonal_speed, shield, x, y, item)

    def shooting(self, bullets, screen):
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
    



class Mob():
    def __init__(self, hp, damage, texture, speed, x, y):
        self.hp = hp
        self.damage = damage
        self.texture = texture
        self.speed = speed
        self.x = x
        self.y = y

    def collision(self):
        pass

    def spawn(map, screen, rooms, cats):
        for x, y in rooms:
            if map[x][y] == 2:
                print(x, y)
                rand = random.randint(0, 4)
                if rand == 1:
                    mob1 = Mob(50, 1, cats, 2, 570, 470)
                    screen.blit(mob1.texture, (mob1.x, mob1.y))
                    # return mob1
                if rand == 2:
                    mob1 = Mob(50, 1, cats, 2, 500, 400)
                    mob2 = Mob(50, 1, cats, 2, 640, 400)
                    screen.blit(mob1.texture, (mob1.x, mob1.y))
                    screen.blit(mob2.texture, (mob2.x, mob2.y))
                    # return mob1, mob2
                if rand == 3:
                    mob1 = Mob(50, 1, cats, 2, 570, 470)
                    mob2 = Mob(50, 1, cats, 2, 500, 400)
                    mob3 = Mob(50, 1, cats, 2, 640, 400)
                    screen.blit(mob1.texture, (mob1.x, mob1.y))
                    screen.blit(mob2.texture, (mob2.x, mob2.y))
                    screen.blit(mob3.texture, (mob3.x, mob3.y))
                    # return mob1, mob2, mob3
                if rand == 4:
                    mob1 = Mob(50, 1, cats, 2, 570, 470)
                    mob2 = Mob(50, 1, cats, 2, 500, 400)
                    mob3 = Mob(50, 1, cats, 2, 640, 400)
                    mob4 = Mob(50, 1, cats, 2, 570, 540)
                    screen.blit(mob1.texture, (mob1.x, mob1.y))
                    screen.blit(mob2.texture, (mob2.x, mob2.y))
                    screen.blit(mob3.texture, (mob3.x, mob3.y))
                    screen.blit(mob4.texture, (mob4.x, mob4.y))
                    # return mob1, mob2, mob3, mob4

class Boss(Enemy):
    def __init__(self, name, hp, damage, texture, x, y):
        super().__init__(name, hp, damage, texture, x, y)


class Arrow:
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 3

    def draw(self, screen):
        pygame.draw.circle(screen, "Red", (self.x, self.y), self.radius)


class Item:
    def __init__(self, texture):
        self.texture = texture
        
    def create_item(gold_x, gold_y, map, item, screen, player):
        if player.shield == False:
            if map[gold_x][gold_y] == 2:
                screen.blit(item, (570, 400))

    def collision(item_hitbox, player, gold_x, gold_y, map, item):
        if player.hitbox.colliderect(item_hitbox):
            if map[gold_x][gold_y] == 2:
                item.use(player)
                player.shield = True
                gold_x, gold_y = 9, 9





class HealthPotion(Item):
    def __init__(self, texture):
        super().__init__(texture)
        self.heal_amount = 1

    def create_item(gold_x, gold_y, map, item, screen):
        if map[gold_x][gold_y] == 2:
            screen.blit(item, (570, 400))

    def use(self, player):
        if player.item == False:
            player.item = True
            player.hp += 1


class SpeedBoost(Item):
    def __init__(self, texture):
        super().__init__(texture)
        self.duration = 0.5

    def create_item(gold_x, gold_y, map, item, screen):
        if map[gold_x][gold_y] == 2:
            screen.blit(item, (570, 400))

    def use(self, player):
        if player.item == False:
            player.item = True
            player.speed += 0.5


class DamageBoost(Item):
    def __init__(self, texture):
        super().__init__(texture)
        self.duration = 2

    def create_item(gold_x, gold_y, map, item, screen):
        if map[gold_x][gold_y] == 2:
            screen.blit(item, (570, 400))

    def use(self, player):
        if player.item == False:
            player.item = True  
            player.damage += 2
