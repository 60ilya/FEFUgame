import pygame

# rooms

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

room_x = 4
room_y = 4

WIDTH = 1280
HEIGHT = 768

running = True

door_up = (534, 164)
door_down = (534, 646)
door_left = (200, 346)
door_right = (1000, 346)

door_up_open = (700, 164)
door_down_open = (368, 646)
door_left_open = (200, 180)
door_right_open = (1000, 512)

mob_leftx = 510
mob_rightx = 650
mob_upx = 580
mob_downx = 580
mob_lefty = 400
mob_righty = 400
mob_upy = 390
mob_downy = 410


#                                                           KEYBOARD SETTINGS
#                                        Example: switch mov_up to key O will be: mov_up = pygame.K_o

#MOVING               
mov_up = pygame.K_w
mov_down = pygame.K_s
mov_left = pygame.K_a
mov_right = pygame.K_d

#SHOOTING
shoot_up = pygame.K_UP
shoot_down = pygame.K_DOWN
shoot_left = pygame.K_LEFT
shoot_right = pygame.K_RIGHT
