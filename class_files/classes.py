import pygame

class Character():
    def __init__(self, texture, hitbox, hp, damage, speed, diagonal_speed, x, y):
        self.texture = texture
        self.hitbox = hitbox
        self.hp = hp
        self.damage = damage
        self.speed = speed
        self.diagonal_speed = diagonal_speed
        self.x = x
        self.y = y
        self.alive = True

    def die(self):
        self.alive = False
        del self

    def take_damage(self, damage):
        self.hp -= damage

    def attack(self, target):
        damage = self.damage
        target.take_damage(damage)
class Player(Character):
    def __init__(self, texture, hitbox, hp, damage, speed, diagonal_speed, shield, x, y):
        super().__init__(texture, hitbox, hp, damage, speed, diagonal_speed, x, y)
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
    def __init__(self, name, hp, damage, texture, hitbox, speed, diagonal_speed, x, y):
        super().__init__(name, texture, hitbox, hp, damage, speed, diagonal_speed, x, y)


class Warrior(Player):
    def __init__(self, texture, hitbox, hp, damage, speed, diagonal_speed, shield, x, y):
        super().__init__(texture, hitbox, hp, damage, speed, diagonal_speed, shield, x, y)




class Archer(Player):
    def __init__(self, texture, hitbox, hp, damage, speed, diagonal_speed, shield, x, y):
        super().__init__(texture, hitbox, hp, damage, speed, diagonal_speed, shield, x, y)
    



class Mob(Enemy):
    def __init__(self, name, hp, damage, texture, hitbox, speed, diagonal_speed, x, y):
        super().__init__(name, hp, damage, texture, hitbox, speed, diagonal_speed, x, y)

    def collision(self):
        pass

class Boss(Enemy):
    def __init__(self, name, hp, damage, texture, x, y):
        super().__init__(name, hp, damage, texture, x, y)


class Arrow:
    def __init__(self, speed, damage):
        self.speed = speed
        self.damage = damage


class Item:
    def __init__(self, texture, hitbox = None):
        self.texture = texture
        
    def create_item(gold_x, gold_y, map, item, screen, player):
        if player.shield == False:
            if map[gold_x][gold_y] == 2:
                screen.blit(item, (570, 400))

    def collision(item_hitbox, player, gold_x, gold_y, map):
        if player.hitbox.colliderect(item_hitbox):
            if map[gold_x][gold_y] == 2:
                player.shield = True
                gold_x, gold_y = 9, 9





class HealthPotion(Item):
    def __init__(self, texture):
        super().__init__(texture)
        self.heal_amount = 1

    def create_item(gold_x, gold_y, map, item, screen):
        if map[gold_x][gold_y] == 2:
            screen.blit(item, (570, 400))

    def use(self, character):
        character.heal(self.heal_amount)


class SpeedBoost(Item):
    def __init__(self, texture):
        super().__init__(texture)
        self.duration = 0.5

    def create_item(gold_x, gold_y, map, item, screen):
        if map[gold_x][gold_y] == 2:
            screen.blit(item, (570, 400))


    def use(self, character):
        character.speed += 0.5


class DamageBoost(Item):
    def __init__(self, texture):
        super().__init__(texture)
        self.duration = 2

    def create_item(gold_x, gold_y, map, item, screen):
        if map[gold_x][gold_y] == 2:
            screen.blit(item, (570, 400))

    def use(self, character):
        character.strength += 2