import pygame
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
    def __init__(self, name, hp, damage, texture, hitbox, speed, diagonal_speed, x, y):
        super().__init__(name, texture, hitbox, hp, damage, speed, diagonal_speed, x, y)

#класс воина
class Warrior(Player):
    def __init__(self, texture, hitbox, hp, damage, speed, diagonal_speed, shield, x, y, item):
        super().__init__(texture, hitbox, hp, damage, speed, diagonal_speed, shield, x, y, item)



#класс лучника
class Archer(Player):
    def __init__(self, texture, hitbox, hp, damage, speed, diagonal_speed, shield, x, y, item):
        super().__init__(texture, hitbox, hp, damage, speed, diagonal_speed, shield, x, y, item)
    


#класс моба
class Mob(Enemy):
    def __init__(self, name, hp, damage, texture, hitbox, speed, diagonal_speed, x, y):
        super().__init__(name, hp, damage, texture, hitbox, speed, diagonal_speed, x, y)

    def collision(self):
        pass
#класс босса
class Boss:
    def __init__(self, texture, hp, damage, x, y):
        self.texture = texture
        self.hp = hp
        self.damage = damage
        self.x = x
        self.y = y
        self.alive = True    

#класс стрелы
class Arrow:
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 3
    #функция рисования
    def draw(self, screen):
        pygame.draw.circle(screen, "Red", (self.x, self.y), self.radius)
#класс предметов
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
