import pygame
import random

pygame.init()

win = pygame.display.set_mode((1500, 800), pygame.RESIZABLE)
clock = pygame.time.Clock()

bots = list()
woods = list()
gifts = list()
inv_snow = list()
big_block = list()
grinch_balls = list()
player_balls = list()
colide_woods = list()
value_of_wall = list()

right = False
left = False
up = False
isJump = False
on_ground = False
jump_count = 10
run = True
fps = 120
speed = 8
x = y = 0
christmas = [False]
player_hp = [1000]
grinch_hp = [10000]
player_value = [True]
count_gifts = [0]
blast_value = [0]
index_of_grinch_blast = [0]
jump_count_grinch = [10]
serial_number = 1
platform_height = 25
platform_width = 25
player_height = 25
player_width = 25
bot_height = 40
bot_width = 40
scroll_value = 20
gift_height = 30
gift_width = 30
wood_height = 25
wood_width = 25

background = pygame.image.load("image.jpg")

# list of invis blocks
block = [
[pygame.Rect(2050, 1200, 950, 25), (100, 100, 255)], [pygame.Rect(2450, 1175, 525, 25), (100, 100, 255)], [pygame.Rect(2475, 1150, 525, 25), (100, 100, 255)], \
[pygame.Rect(2450, 1125, 525, 25), (100, 100, 255)], [pygame.Rect(2500, 1100, 500, 25), (100, 100, 255)], [pygame.Rect(2550, 1075, 425, 25), (100, 100, 255)], \
[pygame.Rect(2575, 1050, 400, 25), (100, 100, 255)], [pygame.Rect(4175, 1275, 600, 175), (100, 100, 255)], [pygame.Rect(4325, 1250, 450, 25), (100, 100, 255)], \
[pygame.Rect(5025, 1250, 325, 25), (100, 100, 255)], [pygame.Rect(5600, 1225, 250, 225), (100, 100, 255)], [pygame.Rect(4950, 1250, 425, 200), (100, 100, 255)], \
[pygame.Rect(4775, 1300, 175, 150), (100, 100, 255)], [pygame.Rect(0, 875, 75, 325), (100, 100, 255)], [pygame.Rect(75, 1075, 75, 125), (100, 100, 255)], \
[pygame.Rect(150, 1150, 50, 50), (100, 100, 255)], [pygame.Rect(200, 1175, 25, 25), (100, 100, 255)], [pygame.Rect(6050, 1300, 3000, 150), (100, 100, 255)], \
[pygame.Rect(6050, 1250, 325, 50), (100, 100, 255)], [pygame.Rect(6700, 1250, 2500, 50), (100, 100, 255)], [pygame.Rect(7375, 1200, 850, 50), (100, 100, 255)], \
[pygame.Rect(7925, 1150, 300, 50), (100, 100, 255)], [pygame.Rect(8125, 1100, 100, 50), (100, 100, 255)], [pygame.Rect(8175, 1050, 50, 50), (100, 100, 255)], \
[pygame.Rect(8175, 700, 50, 275), (100, 100, 255)], [pygame.Rect(8100, 700, 100, 225), (100, 100, 255)], [pygame.Rect(7825, 725, 400, 150), (100, 100, 255)], \
[pygame.Rect(7475, 775, 400, 75), (100, 100, 255)], [pygame.Rect(8200, 725, 5000, 700), (100, 100, 255)], [pygame.Rect(6900, 1025, 475, 50), (100, 100, 255)], \
[pygame.Rect(6825, 975, 1000, 50), (100, 100, 255)], [pygame.Rect(6825, 925, 575, 50), (100, 100, 255)], [pygame.Rect(6750, 900, 550, 50), (100, 100, 255)], \
[pygame.Rect(6750, 900, 500, 50), (100, 100, 255)], [pygame.Rect(6700, 850, 450, 50), (100, 100, 255)], [pygame.Rect(6550, 800, 575, 50), (100, 100, 255)], \
[pygame.Rect(6425, 750, 725, 50), (100, 100, 255)], [pygame.Rect(6375, 700, 850, 50), (100, 100, 255)], [pygame.Rect(6275, 650, 1250, 50), (100, 100, 255)], \
[pygame.Rect(6200, 600, 1725, 50), (100, 100, 255)], [pygame.Rect(6175, 550, 2225, 50), (100, 100, 255)], [pygame.Rect(6125, 500, 2450, 50), (100, 100, 255)], \
[pygame.Rect(6100, 450, 2550, 50), (100, 100, 255)], [pygame.Rect(6075, 400, 2700, 50), (100, 100, 255)], [pygame.Rect(6000, 350, 2900, 50), (100, 100, 255)], \
[pygame.Rect(5950, 300, 3075, 50), (100, 100, 255)], [pygame.Rect(5850, 250, 3250, 50), (100, 100, 255)], [pygame.Rect(5775, 200, 3400, 50), (100, 100, 255)], \
[pygame.Rect(5725, 150, 3550, 50), (100, 100, 255)], [pygame.Rect(5675, 100, 3700, 50), (100, 100, 255)],
[pygame.Rect(11525, 300, 100, 25), (0, 0, 0)]
]


# collide block's
blocks = [
[pygame.Rect(200, 1175, 1300, 25), (255, 255, 255)], [pygame.Rect(1500, 1425, 525, 25), (255, 255, 255)], [pygame.Rect(2025, 1175, 425, 25), (255, 255, 255)], \
[pygame.Rect(2550, 1025, 450, 25), (255, 255, 255)], [pygame.Rect(3000, 1225, 1175, 25), (255, 255, 255)], [pygame.Rect(4175, 1250, 150, 25), (255, 255, 255)], \
[pygame.Rect(4325, 1225, 400, 25), (255, 255, 255)], [pygame.Rect(4775, 1275, 175, 25), (255, 255, 255)], [pygame.Rect(5025, 1225, 350, 25), (255, 255, 255)], \
[pygame.Rect(5600, 1225, 250, 25), (255, 255, 255)], [pygame.Rect(5375, 1425, 225, 25), (255, 255, 255)], [pygame.Rect(5850, 1425, 200, 25), (255, 255, 255)], \
[pygame.Rect(6050, 1225, 275, 25), (255, 255, 255)], [pygame.Rect(6375, 1275, 325, 25), (255, 255, 255)], [pygame.Rect(6750, 1225, 625, 25), (255, 255, 255)], \
[pygame.Rect(6750, 1225, 625, 25), (255, 255, 255)], [pygame.Rect(7375, 1200, 325, 25), (255, 255, 255)], [pygame.Rect(7700, 1175, 225, 25), (255, 255, 255)], \
[pygame.Rect(8050, 700, 5150, 25), (255, 255, 255)], [pygame.Rect(7925, 1150, 125, 25), (255, 255, 255)], [pygame.Rect(8050, 1125, 75, 25), (255, 255, 255)], \
[pygame.Rect(6925, 1075, 175, 25), (255, 255, 255)], [pygame.Rect(7100, 1050, 275, 25), (255, 255, 255)], [pygame.Rect(7375, 1025, 400, 25), (255, 255, 255)], \
[pygame.Rect(7775, 1000, 250, 25), (255, 255, 255)], [pygame.Rect(7650, 975, 350, 25), (255, 255, 255)], [pygame.Rect(7400, 950, 250, 25), (255, 255, 255)], \
[pygame.Rect(7725, 850, 350, 25), (255, 255, 255)], [pygame.Rect(7475, 825, 250, 25), (255, 255, 255)], [pygame.Rect(7300, 800, 175, 25), (255, 255, 255)], \
[pygame.Rect(7350, 775, 250, 25), (255, 255, 255)], [pygame.Rect(7600, 750, 225, 25), (255, 255, 255)], [pygame.Rect(7825, 725, 225, 25), (255, 255, 255)], \
[pygame.Rect(7300, 925, 100, 25), (255, 255, 255)], [pygame.Rect(7200, 900, 100, 25), (255, 255, 255)], [pygame.Rect(7250, 675, 275, 25), (255, 255, 255)], \
[pygame.Rect(7525, 650, 275, 25), (255, 255, 255)], [pygame.Rect(7800, 625, 125, 25), (255, 255, 255)], [pygame.Rect(7925, 600, 75, 25), (255, 255, 255)], \
[pygame.Rect(8000, 575, 225, 25), (255, 255, 255)], [pygame.Rect(8225, 600, 125, 25), (255, 255, 255)], [pygame.Rect(8400, 550, 125, 25), (255, 255, 255)], \
[pygame.Rect(8650, 675, 150, 25), (255, 255, 255)], [pygame.Rect(9125, 675, 125, 25), (255, 255, 255)], [pygame.Rect(9150, 650, 100, 25), (255, 255, 255)], \
[pygame.Rect(10275, 675, 200, 25), (255, 255, 255)], [pygame.Rect(10300, 650, 130, 25), (255, 255, 255)], [pygame.Rect(10600, 550, 75, 25), (255, 255, 255)], \
[pygame.Rect(10300, 450, 75, 25), (255, 255, 255)], [pygame.Rect(10100, 350, 75, 25), (255, 255, 255)], [pygame.Rect(10400, 300, 75, 25), (255, 255, 255)], \
[pygame.Rect(10600, 225, 75, 25), (255, 255, 255)], [pygame.Rect(10800, 150, 75, 25), (255, 255, 255)], [pygame.Rect(11000, 75, 75, 25), (255, 255, 255)], \
[pygame.Rect(11200, 0, 75, 25), (255, 255, 255)], [pygame.Rect(11200, 300, 25, 400), (255, 255, 255)], [pygame.Rect(12200, 300, 25, 400), (255, 255, 255)], \
[pygame.Rect(11225, 300, 300, 25), (255, 255, 255)], [pygame.Rect(11625, 300, 575, 25), (255, 255, 255)], [pygame.Rect(11625, 150, 25, 150), (100, 100, 255)], \
[pygame.Rect(11500, 150, 25, 150), (100, 100, 255)], [pygame.Rect(11475, 125, 75, 25), (100, 100, 255)], [pygame.Rect(11600, 125, 75, 25), (100, 100, 255)], \
[pygame.Rect(75, 875, 25, 200), (100, 100, 255)], [pygame.Rect(1475, 1200, 25, 225), (100, 100, 255)], [pygame.Rect(2025, 1200, 25, 225), (100, 100, 255)], \
[pygame.Rect(2975, 1050, 25, 175), (100, 100, 255)], [pygame.Rect(5600, 1250, 25, 175), (100, 100, 255)], [pygame.Rect(5350, 1250, 25, 175), (100, 100, 255)], \
[pygame.Rect(6050, 1250, 25, 175), (100, 100, 255)], [pygame.Rect(5825, 1250, 25, 175), (100, 100, 255)]]

player = pygame.Rect(160, 700, player_width, player_height)
grinch = [
[pygame.Rect(9700, 675, 25, 25), (173, 255, 47), 0, 50, 0, 75], [pygame.Rect(9750, 675, 25, 25), (173, 255, 47), 50, 0, 0, 75], [pygame.Rect(9725, 650, 25, 25), (173, 255, 47), 25, 25, 25, 50],
[pygame.Rect(9725, 625, 25, 25), (173, 255, 47), 25, 25, 50, 25], [pygame.Rect(9700, 625, 25, 25), (173, 255, 47), 0, 50, 50, 25], [pygame.Rect(9750, 625, 25, 25), (173, 255, 47), 50, 0, 50, 255],
[pygame.Rect(9725, 600, 25, 25), (173, 251, 152), 25, 25, 75, 0]]

level = open("layer.txt", "r").read().split("\n")

for platforms in level:
    for platform in platforms:
        if platform == "8":
            big_block.append([pygame.Rect(x, y, 2150, 225), (100, 100, 255)])

        if platform == "9":
            big_block.append([pygame.Rect(x, y, 1500, 250), (100, 100, 255)])

        if platform == "-":
            blocks.append([pygame.Rect(x, y, platform_width, platform_height), (100, 100, 255)])

        if platform == "1":
            blocks.append([pygame.Rect(x, y, platform_width, platform_height), (255, 255, 255)])

        if platform == "0":
            gifts.append([pygame.Rect(x, y-5, gift_width, gift_height), (0, 255, 0)])

        if platform == "b":
            bots.append([pygame.Rect(x, y-15, bot_width, bot_height), (148, 0, 211), serial_number])
            serial_number += 1

        if platform == "=":
            colide_woods.append([pygame.Rect(x, y, wood_width, wood_height), (255, 255, 255)])

        if platform == "+":
            woods.append([pygame.Rect(x, y, wood_width, wood_height), (61,43,31)])

        if platform == ")":
            woods.append([pygame.Rect(x, y, wood_width, wood_height), (0,100,0)])

        if platform == "i":
            inv_snow.append([pygame.Rect(x, y, wood_width, wood_height), (255, 255, 255)])

        x += platform_width
    y += platform_height
    x = 0

blocks += colide_woods
index_value_for_bots = [0 for i in range(len(bots))]

blocks.append([pygame.Rect(8275, 675, 25, 25), (255, 255, 255)])
blocks.append([pygame.Rect(8275, 650, 25, 25), (255, 255, 255)])
blocks.append([pygame.Rect(8275, 625, 25, 25), (255, 255, 255)])

# bot's settings
bots[0].append((8, index_value_for_bots, 0.2, 10, 20, 40, 10))
bots[1].append((8, index_value_for_bots, 0.2, 10, 20, 30, 5))
bots[2].append((8, index_value_for_bots, 0.2, 10, 20, 30, 7))
bots[3].append((8, index_value_for_bots, 0.2, 10, 20, 30, 10))
bots[4].append((8, index_value_for_bots, 0.2, 10, 20, 30, 20))
bots[5].append((8, index_value_for_bots, 0.2, 10, 20, 30, 6))
bots[6].append((8, index_value_for_bots, 0.2, 10, 20, 30, 7))
bots[7].append((8, index_value_for_bots, 0.2, 10, 20, 30, 9))
bots[8].append((8, index_value_for_bots, 0.2, 10, 20, 30, 10))

def collision_test(player, blocks):
    collisions = list()
    for i in blocks:
        if player.colliderect(i[0]):
            collisions.append(i[0])

    return collisions

def get_damege(player, grinch_balls):
    for ball in grinch_balls:
        if player.colliderect(ball[0]):
            player_hp[0] -= 200
            grinch_balls.remove(ball)

def blast_of_grinch(player, grinch, grinch_balls, blocks):
    index = random.randint(0, 1)
    place_blast_left = random.randint(1, 4)
    place_blast_right = random.randint(1, 4)

    left_dict = {1: grinch[4][0].x - 25, 2: grinch[3][0].x - 25, 3: grinch[2][0].x - 25, 4: grinch[0][0].x}
    right_dict = {1: grinch[4][0].x + 25, 2: grinch[3][0].x + 25, 3: grinch[2][0].x + 25, 4: grinch[1][0].x}

    left_dict_y = {1: grinch[4][0].y, 2: grinch[3][0].y, 3: grinch[2][0].y, 4: grinch[0][0].y}
    right_dict_y = {1: grinch[4][0].y, 2: grinch[3][0].y, 3: grinch[2][0].y, 4: grinch[1][0].y}

    if int(index_of_grinch_blast[0]) == 10:
        if index == 0:
            grinch_balls.append([pygame.Rect(left_dict[place_blast_left], left_dict_y[place_blast_left], 25, 25), (255, 255, 255), [False]])
        else:
            grinch_balls.append([pygame.Rect(right_dict[place_blast_right], right_dict_y[place_blast_right], 25, 25), (255, 255, 255), [True]])

        index_of_grinch_blast[0] = 0

    for on in grinch_balls:
        if on[2][0] == False:
            on[0].move_ip(-4, 0)
        else:
            on[0].move_ip(4, 0)

    for ball in grinch_balls:
        col = collision_test(ball[0], blocks)

        if col != []:
            grinch_balls.remove(ball)

    index_of_grinch_blast[0] += 0.7

def move_grinch(grinch, blocks):
    jump_grinch = True if random.randint(0, 10) == 1 else False
    movement_grinch = [random.randint(-10, 10), 0]

    if not jump_grinch:
        jump_grinch = True
    else:
        movement_grinch[1] -= jump_count_grinch[0]
        jump_count_grinch[0] -= 1

        if jump_count_grinch[0] < -10:
            jump_grinch = False
            jump_count_grinch[0] = 10

    for gri in grinch:
        if gri[0].x >= 10275:
            gri[0].x -= movement_grinch[0]
        else:
            gri[0].x += movement_grinch[0]

        if gri[0].x <= 9225:
            gri[0].x += movement_grinch[0]
        else:
            gri[0].x -= movement_grinch[0]

        col = collision_test(gri[0], blocks)

        for i in col:
            if movement_grinch[0] > 0:
                for main in grinch:
                    main[0].right = i.left - main[3]

            if movement_grinch[0] < 0:
                for main in grinch:
                    main[0].left = i.right + main[2]

        gri[0].y += movement_grinch[1]
        coll = collision_test(gri[0], blocks)

        if coll != []:
            grinch_on_ground = True
        else:
            grinch_on_ground = False

        for u in coll:
            if movement_grinch[1] > 0:
                for main in grinch:
                    main[0].bottom = u.top - main[4]

            if movement_grinch[1] < 0:
                for main in grinch:
                    main[0].top = u.bottom + main[5]

    print_text(f"Grinch: {str(grinch_hp)[1:-1]}", grinch[-1][0].x - 100, grinch[-1][0].y - 50, (255, 0, 255), 50)

    return grinch

def collision_balls(list_of_balls, blocks, grinch):
    for i in list_of_balls:
        collision = collision_test(i[0], blocks)
        if collision != []:
            list_of_balls.remove(i)

    for x in list_of_balls:
        collision = collision_test(x[0], grinch)
        if collision != []:
            list_of_balls.remove(x)
            grinch_hp[0] -= 500

def main_function_of_bots_movement_right(bot, blocks):
    collision = collision_test(bot[0], blocks)
    for i in collision:
        bot[0].left = i.right

    return bot[0]

def main_function_of_bots_movement_left(bot, blocks):
    collision = collision_test(bot[0], blocks)
    for i in collision:
        bot[0].right = i.left

    return bot[0]

def bots_movement(player, blocks, bot, bot_number, bot_speed, index_value_for_bots, biggr_index, firsst_index, second_index, third_index, iterations):
    index_value_for_bots[bot_number-1] += biggr_index
    on_ground = False

    if int(index_value_for_bots[bot_number-1]) == firsst_index:
        for i in range(iterations):
            bot[0].x += bot_speed
            bot[0] = main_function_of_bots_movement_left(bot, blocks)

    if int(index_value_for_bots[bot_number-1]) == second_index:
        for i in range(iterations):
            bot[0].x += -bot_speed
            bot[0] = main_function_of_bots_movement_right(bot, blocks)

    if int(index_value_for_bots[bot_number-1]) == third_index:
        index_value_for_bots[bot_number-1] = 0

    bot[0].y += 10
    col = collision_test(bot[0], blocks)

    for i in col:
        bot[0].bottom = i.top

    return bot

def print_text(messemge, x, y, font_color=(0,0,0), font_size=0):
    font_types = pygame.font.Font(None, font_size)
    text = font_types.render(messemge, True, font_color)
    win.blit(text, (x, y))

def put_the_gift(player, gifts, count_gifts):
    for g in gifts:
        if player.colliderect(g[0]):
            gifts.remove(g)
            count_gifts[0] += 1

def move(player, movement, blocks, bots):
    player.x += movement[0]
    collisions = collision_test(player, blocks)
    col_for_bot = collision_test(player, bots)
    on_ground = False

    for i in collisions:
        if movement[0] > 0:
            player.right = i.left
        if movement[0] < 0:
            player.left = i.right

    for i in col_for_bot:
        if movement[0] > 0:
            player.right = i.left
            player_hp[0] -= 20
        if movement[0] < 0:
            player.left = i.right
            player_hp[0] -= 20

    scroll[0] -= (player.x + scroll[0] - 750) / scroll_value

    for i in player_balls:
        i[0].move_ip(scroll[0], 0)

    for gr in grinch:
        gr[0].move_ip(scroll[0], 0)

    for bl in block:
        bl[0].move_ip(scroll[0], 0)

    for bb in big_block:
        bb[0].move_ip(scroll[0], 0)

    for inv in inv_snow:
        inv[0].move_ip(scroll[0], 0)

    for qwer in woods:
        qwer[0].move_ip(scroll[0], 0)

    for x in blocks:
        x[0].move_ip(scroll[0], 0)

    for uu in gifts:
        uu[0].move_ip(scroll[0], 0)

    for fpr in bots:
        fpr[0].move_ip(scroll[0], 0)

    for ii in grinch_balls:
        ii[0].move_ip(scroll[0], 0)

    player.move_ip(scroll[0], 0)

    player.y += movement[1]
    col = collision_test(player, blocks)
    col_for_bot = collision_test(player, bots)

    if col != [] or col_for_bot != []:
        on_ground = True
    else:
        on_ground = False

    for x in col:
        if movement[1] > 0:
            player.bottom = x.top
        if movement[1] < 0:
            player.top = x.bottom

    for i in col_for_bot:
        if movement[1] > 0:
            player.y -= 100
            movement[1] += -100
            player.move_ip(0, -100)

    scroll[0] -= (player.x - scroll[0] - 750) / scroll_value

    for i in player_balls:
        i[0].move_ip(scroll[0], 0)

    for gr in grinch:
        gr[0].move_ip(scroll[0], 0)

    for bl in block:
        bl[0].move_ip(scroll[0], 0)

    for bb in big_block:
        bb[0].move_ip(scroll[0], 0)

    for inv in inv_snow:
        inv[0].move_ip(scroll[0], 0)

    for qwer in woods:
        qwer[0].move_ip(scroll[0], 0)

    for x in blocks:
        x[0].move_ip(scroll[0], 0)

    for uu in gifts:
        uu[0].move_ip(scroll[0], 0)

    for fpr in bots:
        fpr[0].move_ip(scroll[0], 0)

    for ii in grinch_balls:
        ii[0].move_ip(scroll[0], 0)

    player.move_ip(scroll[0], 0)

    return player, on_ground

while run:
    scroll = [0,0]
    movement = [0,0]

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False

    if left == True:
        movement[0] -= speed

    if right == True:
        movement[0] += speed

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        left = True
        player_value[0] = False
    else:
        left = False

    if keys[pygame.K_RIGHT]:
        right = True
        player_value[0] = True
    else:
        right = False

    blast_value[0] += 1

    if keys[pygame.K_p]:
        if int(blast_value[0]) >= 10:
            player_balls.append([pygame.Rect(player.x + player_width if player_value[0] == True else player.x - player_width, player.y, 25, 25), (255, 0, 255), player_value[0]])
            blast_value[0] = 0

    for i in player_balls:
        if i[2] == False:
            i[0].move_ip(-6, 0)
        if i[2] == True:
            i[0].move_ip(6, 0)

    # jump
    if not isJump:
        if keys[pygame.K_UP] and on_ground == True:
            isJump = True
        else:
            movement[1] += 10
            scroll[1] -= (player.y + scroll[0] - 400) / scroll_value

            for gr in grinch:
                gr[0].move_ip(0, scroll[1])

            for bl in block:
                bl[0].move_ip(0, scroll[1])

            for bb in big_block:
                bb[0].move_ip(0, scroll[1])

            for inv in inv_snow:
                inv[0].move_ip(0, scroll[1])

            for qwer in woods:
                qwer[0].move_ip(0, scroll[1])

            for u in blocks:
                u[0].move_ip(0, scroll[1])

            for uu in gifts:
                uu[0].move_ip(0, scroll[1])

            for fpr in bots:
                fpr[0].move_ip(0, scroll[1])

            for i in player_balls:
                i[0].move_ip(0, scroll[1])

            for ii in grinch_balls:
                ii[0].move_ip(0, scroll[1])

            player.move_ip(0, scroll[1])

    else:
        movement[1] -= jump_count
        scroll[1] -= (player.y - scroll[0] - 400) / scroll_value

        for gr in grinch:
            gr[0].move_ip(0, scroll[1])

        for bl in block:
            bl[0].move_ip(0, scroll[1])

        for bb in big_block:
            bb[0].move_ip(0, scroll[1])

        for inv in inv_snow:
            inv[0].move_ip(0, scroll[1])

        for qwer in woods:
            qwer[0].move_ip(0, scroll[1])

        for u in blocks:
            u[0].move_ip(0, scroll[1])

        for uu in gifts:
            uu[0].move_ip(0, scroll[1])

        for fpr in bots:
            fpr[0].move_ip(0, scroll[1])

        for i in player_balls:
            i[0].move_ip(0, scroll[1])

        for ii in grinch_balls:
            ii[0].move_ip(0, scroll[1])

        player.move_ip(0, scroll[1])
        jump_count -= 1

        if jump_count < -10:
            isJump = False
            jump_count = 10

    # collisions
    player = move(player, movement, blocks, bots)[0]
    check = move(player, movement, blocks, bots)[1]

    if check == True:
        on_ground = True
    else:
        on_ground = False

    # drawing on the display
    win.fill((0,0,0))
    win.blit(background, (0,0))

    for qwer in woods:
        pygame.draw.rect(win, qwer[1], qwer[0])

    pygame.draw.rect(win, (255, 0, 0), player)
    put_the_gift(player, gifts, count_gifts)

    for b in block:
        pygame.draw.rect(win, b[1], b[0])

    for inv in inv_snow:
        pygame.draw.rect(win, inv[1], inv[0])

    for bb in big_block:
        pygame.draw.rect(win, bb[1], bb[0])

    for i in blocks:
        pygame.draw.rect(win, i[1], i[0])

    for gift in gifts:
        pygame.draw.rect(win, gift[1], gift[0])

    for boooooooooot in bots:
        pygame.draw.rect(win, boooooooooot[1], boooooooooot[0])

    for number in bots:
        print_text(f"{number[2]}", number[0].x + 10, number[0].y, (255, 255, 0), 60)

    for gr in grinch:
        pygame.draw.rect(win, gr[1], gr[0])

    for i in player_balls:
        pygame.draw.rect(win, i[1], i[0])

    # bots movement and colisions
    for bot in range(len(bots)):
        bots[bot] = bots_movement(player, blocks, bots[bot], bots[bot][2], bots[bot][3][0], bots[bot][3][1], bots[bot][3][2], bots[bot][3][3], bots[bot][3][4], bots[bot][3][5], bots[bot][3][6])

    # count of gifts
    print_text(str(count_gifts)[1:-1], 1450 - len(str(count_gifts[0])) * 20, 0, (0,255,0), 100)
    print_text(f"HP: {str(player_hp)[1:-1]}" , 0, 0, (0, 255, 0), 100)
    collision_balls(player_balls, blocks, grinch)

    if player_hp[0] <= 0:
        print("Game ending...")
        quit()

    if grinch_hp[0] <= 0:
        grinch = list()
        grinch_balls = list()

        for i in block:
            if i[1] == (0,0,0) and player.colliderect(i[0]) == 1:
                christmas[0] = True
                block.remove(i)

    if christmas[0] == True:
        print_text("Christmas saved!", 300, 300, (0, 255, 0), 150)

    if grinch != []:
        grinch = move_grinch(grinch, blocks)
        blast_of_grinch(player, grinch, grinch_balls, blocks)

    if count_gifts[0] == 10:
        value_of_wall.append(1)

    if len(value_of_wall) == 1:
        for i in range(1, 3):
            blocks.remove(blocks[-i])

    for i in grinch_balls:
        pygame.draw.rect(win, i[1], i[0])

    get_damege(player, grinch_balls)

    # update
    clock.tick(fps)
    pygame.time.delay(10)
    pygame.display.update()
