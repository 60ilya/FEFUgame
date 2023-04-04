from const import L, R, U, D, DL, UD, UDL, UL, UR, URD, URDL, URL, RD, RDL, RL
import random
import math

class Game():
    #проверка массива для миникарты
    def array_check(map, x, y, n):
        if map[x][y] == 1: #            (8, 2)
            if y + 1 < 9 and map[x][y + 1] == 0: # check R
                if map[x][y + 2] == 0 and map[x + 1][y + 1] == 0 and map[x - 1][y + 1] == 0: # check RDU
                    map[x][y + 1] = n
            elif y - 1 > -1 and map[x][y - 1] == 0: # check L
                if map[x][y - 2] == 0 and map[x + 1][y - 1] == 0 and map[x - 1][y - 1] == 0: # check LDU
                    map[x][y - 1] = n
            elif x + 1 < 9 and map[x + 1][y] == 0: # check D
                if map[x + 2][y] == 0 and map[x + 1][y + 1] == 0 and map[x + 1][y - 1] == 0: # check DRL
                    map[x + 1][y] = n
            elif x - 1 > -1 and map[x - 1][y] == 0: # check U
                if map[x - 2][y] == 0 and map[x - 1][y + 1] == 0 and map[x - 1][y - 1] == 0: # check URL
                    map[x - 1][y] = n
    class map():#создание невидимого блока
        def room_inv_block(map, x, y, player):
            if map[x - 1][y] == 0:
                if player.y < 222:
                    player.y = 223
            if map[x + 1][y] == 0:
                if player.y > 614:
                    player.y = 613
            if map[x][y - 1] == 0:
                if player.x < 244:
                    player.x = 245
            if map[x][y + 1] == 0:
                if player.x > 972:
                    player.x = 971
        #согдание карндомной карты
        def rand_map():
            count = 0
            flag = False

            while 1:
                flag = False
                count = 0
                map = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

                def up(map, i, j, n):
                    map[i - 1][j] = n
                    
                def down(map, i, j, n):
                    map[i + 1][j] = n

                def left(map, i, j, n):
                    map[i][j - 1] = n

                def right(map, i, j, n):
                    map[i][j + 1] = n

                for z in range(5):
                    for i in range(0, 9):
                        for j in range(0, 9):
                            if map[i][j] != 0:
                                func = random.choice([0, 1, 2, 3])
                                if i == 0 and j == 0:
                                    if func == 1:
                                        right(map, i, j, 1)

                                    elif func == 2:
                                        left(map, i, j, 1)
                                    break

                                elif i == 0 and j == 9:
                                    if func == 2:
                                        left(map, i, j, 1)

                                    elif func == 3:
                                        down(map, i, j, 1)
                                    break

                                elif i == 9 and j == 9:
                                    if func == 0:
                                        up(map, i, j, 1)

                                    elif func == 2:
                                        left(map, i, j, 1)
                                    break

                                elif i == 9 and j == 0:
                                    if func == 0:
                                        up(map, i, j, 1)

                                    elif func == 1:
                                        right(map, i, j, 1)
                                    break

                                elif i == 0:

                                    if func == 1:
                                        right(map, i, j, 1)

                                    elif func == 2:
                                        left(map, i, j, 1)

                                    elif func == 3:
                                        down(map, i, j, 1)
                                    break

                                elif i == 9:
                                    if func == 0:
                                        up(map, i, j, 1)

                                    elif func == 1:
                                        right(map, i, j, 1)

                                    elif func == 2:
                                        left(map, i, j, 1)
                                    break

                                elif j == 0:
                                    if func == 0:
                                        up(map, i, j, 1)

                                    elif func == 1:
                                        right(map, i, j, 1)

                                    elif func == 3:
                                        down(map, i, j, 1)
                                    break

                                elif j == 9:
                                    if func == 0:
                                        up(map, i, j, 1)
                            
                                    elif func == 2:
                                        left(map, i, j, 1)
                                        
                                    elif func == 3:
                                        down(map, i, j, 1)
                                    break

                                else:
                                    if func == 0:
                                        up(map, i, j, 1)

                                    elif func == 1:
                                        right(map, i, j, 1)

                                    elif func == 2:
                                        left(map, i, j, 1)

                                    elif func == 3:
                                        down(map, i, j, 1)
                                    break
                map[4][4] = 2

                for i in range(10):
                    for j in range(10):
                        if map[i][j] != 0:
                            count += 1
                if count >= 12:
                    for i in range(10):
                        if 1 not in map[9] and 1 not in map[0]:
                            flag = True

                
            

                max_x = 0
                max_y = 0
                max_ans = 0

                for y in range(0, 9):
                    for x in range(0, 9):
                        if map[x][y] == 1:
                            ans = math.sqrt(pow(abs(4 - x), 2) + pow(abs(4 - y), 2))
                            if ans > max_ans:
                                max_ans = ans
                                max_x = x
                                max_y = y

                print(f"boss room x - {max_x}, y - {max_y}")
                Game.array_check(map, max_x, max_y, 4)
                

                max_x = 0
                max_y = 0
                max_ans = 0
                ans = 0

                for y in range(0, 9):
                    for x in range(0, 9):
                        if map[x][y] == 1 and map[x + 1][y] != 4 and map[x - 1][y] != 4 and map[x][y + 1] != 4 and map[x][y - 1] != 4:
                            ans = math.sqrt(pow(abs(4 - x), 2) + pow(abs(4 - y), 2))
                            if ans > max_ans:
                                max_ans = ans
                                max_x = x
                                max_y = y

                print(f"treasure room x - {max_x}, y - {max_y}")
                Game.array_check(map, max_x, max_y, 5)
                

                print("""                     0 - комнаты нет
                        1 - непройденная комната
                        2 - персонаж
                        3 - пройденная комната
                        4 - босс
                        5 - предмет""")
                for i in range(10):
                    print(map[i])
                print()


                boss = False
                item = False

                for y in range(10):
                    for x in range(10):
                        if map[x][y] == 4:
                            boss = True
                for y in range(10):
                    for x in range(10):     
                        if map[x][y] == 5:
                            item = True

                if flag == True and boss == True and item == True:
                    break
            
                

            return map 
        

        #выбор комнаты
        def room_choose(map, i, j):

            if map[i + 1][j] == 0 and map[i - 1][j] == 0 and map[i][j + 1] == 0 and map[i][j - 1] != 0:
                return L
    
            elif map[i + 1][j] == 0 and map[i - 1][j] == 0 and map[i][j + 1] != 0 and map[i][j - 1] == 0:
                return R

            elif map[i + 1][j] == 0 and map[i - 1][j] == 0 and map[i][j + 1] != 0 and map[i][j - 1] != 0:
                return RL

            elif map[i + 1][j] == 0 and map[i - 1][j] != 0 and map[i][j + 1] == 0 and map[i][j - 1] == 0:
                return U

            elif map[i + 1][j] == 0 and map[i - 1][j] != 0 and map[i][j + 1] == 0 and map[i][j - 1] != 0:
                return UL

            elif map[i + 1][j] == 0 and map[i - 1][j] != 0 and map[i][j + 1] != 0 and map[i][j - 1] == 0:
                return UR

            elif map[i + 1][j] == 0 and map[i - 1][j] != 0 and map[i][j + 1] != 0 and map[i][j - 1] != 0:
                return URL

            elif map[i + 1][j] != 0 and map[i - 1][j] == 0 and map[i][j + 1] == 0 and map[i][j - 1] == 0:
                return D

            elif map[i + 1][j] != 0 and map[i - 1][j] == 0 and map[i][j + 1] == 0 and map[i][j - 1] != 0:
                return DL

            elif map[i + 1][j] != 0 and map[i - 1][j] == 0 and map[i][j + 1] != 0 and map[i][j - 1] == 0:
                return RD
            
            elif map[i + 1][j] != 0 and map[i - 1][j] == 0 and map[i][j + 1] != 0 and map[i][j - 1] != 0:
                return RDL

            elif map[i + 1][j] != 0 and map[i - 1][j] != 0 and map[i][j + 1] == 0 and map[i][j - 1] == 0:
                return UD

            elif map[i + 1][j] != 0 and map[i - 1][j] != 0 and map[i][j + 1] == 0 and map[i][j - 1] != 0:
                return UDL

            elif map[i + 1][j] != 0 and map[i - 1][j] != 0 and map[i][j + 1] != 0 and map[i][j - 1] == 0:
                return URD

            elif map[i + 1][j] != 0 and map[i - 1][j] != 0 and map[i][j + 1] != 0 and map[i][j - 1] != 0:
                return URDL


        def get_boss_xy(map):
            for y in range(10):
                for x in range(10):
                    if map[x][y] == 4:
                        return x, y
                    # else:
                    #     return 0, 0