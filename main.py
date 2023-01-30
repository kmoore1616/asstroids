# Import and initialize the pygame library
import pygame
import time
import random
pygame.init()

# General Vars
x = 50  # X Pos of Ship
y = 50  # Y Pos of Ship
shoot = False  # Starts the firing from the ship
vel_y = 0  # Sets the speed of the ship
vel_x = 0
acc = .25  # Is added to vel_x and y to create inertia
lives = 5
game_over = False
draws = -250
draw = -250
exploded = False
new_time = 0
x_1 = x
y_1 = y
game = -200
game_1 = -200
y_mover = 0
y_mover_1 = 0
y_mover_2 = 0
y_mover_3 = 0
x_mover = 0
x_mover_1 = 0
x_mover_2 = 0
x_mover_3 = 0
# sass_moving = False
# sass_moving_1 = False
# sass_moving_2 = False
# sass_moving_3 = False
# sass_mover_x = 0
# sass_mover_x_1 = 0
# sass_mover_x_2 = 0
# sass_mover_x_3 = 0
# sass_mover_y = 0
# sass_mover_y_1 = 0
# sass_mover_y_2 = 0
# sass_mover_y_3 = 0
new_score = False
score_writer = ""
started = False
menu_pos = 1

width = 500  # Width of map
height = 500  # Height of map
n_going_left = False  # Keeps going direction for when shooting
n_going_right = False
n_going_up = False
n_going_down = False
bounce_x = True  # Used in bounce
bounce_y = True

starter = -45

shoot_x = -100  # Marks the starting cords of the bullet
shoot_y = -100  # Marks the starting cords of the bullet
shooting = False  # Tells if bullet is moving
bul_color = 0  # Makes bullet transparent until moving. So it doesn't overlap the ship
shoot_vel = 50  # The velocity of the bullet
bul_going = 0  # Used to save which direction the bullet is moving, so it doesn't change in flight

going_right = False  # Stores last move to tell bullet which direction to go
going_left = False
going_up = False
going_down = False
spot_pick = 0
spot_pick_1 = 0
spot_pick_2 = 0
spot_pick_3 = 0

ship_1 = 450
ship_2 = 450
ship_3 = 450
ship_4 = 450
ship_5 = 450

direct = ""
ax_1 = starter
ay_1 = starter
ax_2 = starter
ay_2 = starter
ax_3 = starter
ay_3 = starter
ax_4 = starter
ay_4 = starter
ax_5 = starter
ay_5 = starter
ax_6 = starter
ay_6 = starter
ax_7 = starter
ay_7 = starter
ax_8 = starter
ay_8 = starter
ax_9 = starter
ay_9 = starter
ax_10 = starter
ay_10 = starter
ax_11 = starter
ay_11 = starter
ax_12 = starter
ay_12 = starter

as_move = False
as_move_2 = False
as_move_3 = False
as_move_4 = False
x_move_pos = False
y_move_pos = False
x_move_pos_1 = False
y_move_pos_1 = False
x_move_pos_2 = False
y_move_pos_2 = False
x_move_pos_3 = False
y_move_pos_3 = False

pos_1 = (-50, -50)
pos_2 = (-50, 200)
pos_3 = (-50, 500)
pos_4 = (100, -50)
pos_5 = (400, -50)
pos_6 = (550, 250)
pos_7 = (550, 470)
pos_8 = (80, 550)
pos_9 = (200, 550)
pos_10 = (400, 550)

difficulty = 25
score = 0
total_time = 0
start_time = time.time()
score_time = total_time + 10

# Set up the drawing window
win = pygame.display.set_mode([width, height])
pygame.display.set_caption("Stroids")

# Imported Images From Assets
bass_1 = pygame.image.load("BASS_1.png").convert()
bass_2 = pygame.image.load("BASS_2.png").convert()
bass_3 = pygame.image.load("BASS_3.png").convert()
bass_4 = pygame.image.load("BASS_4.png").convert()
sass_1 = pygame.image.load("SASS_1.png").convert()
sass_2 = pygame.image.load("SASS_2.png").convert()
sass_3 = pygame.image.load("SASS_3.png").convert()
sass_4 = pygame.image.load("SASS_4.png").convert()
ship = pygame.image.load("Shipp.png").convert()
ship_dd = pygame.image.load("Shipp_Down_Down_L.png").convert()
ship_d_r = pygame.image.load("Shipp_Down_L.png").convert()
ship_d_l = pygame.image.load("Shipp_Down_R.png").convert()
ship_l = pygame.image.load("Shipp_R.png").convert()
ship_u_r = pygame.image.load("Shipp_Up_L.png").convert()
ship_u_l = pygame.image.load("Shipp_Up_R.png").convert()
ship_u_u_r = pygame.image.load("Shipp_Up_Up_L.png").convert()
explosion = pygame.image.load("explosion.jpg").convert()
ship_icon = pygame.image.load('Shipp_icon.png').convert()
title_screen = pygame.image.load('Title_Screen.png').convert()

shipps = ship

crazy_1 = bass_1
crazy_2 = bass_2
crazy_3 = bass_4
crazy_4 = bass_4

in_leader_board = False
#f = open('Hi_Scores.txt', 'r')
#leader_boards = f.readlines()
#leader_1 = leader_boards[0]
#leader_score_1 = leader_1[0:9]
#leader_name_1 = leader_1[9:-1]

#leader_2 = leader_boards[1]
#leader_score_2 = leader_2[0:9]
#leader_name_2 = leader_2[9:-1]

#leader_3 = leader_boards[2]
#leader_score_3 = leader_3[0:9]
#leader_name_3 = leader_3[9:-1]

#leader_4 = leader_boards[3]
#leader_score_4 = leader_4[0:9]
#leader_name_4 = leader_4[9:-1]

#leader_5 = leader_boards[4]
#leader_score_5 = leader_5[0:9]
#leader_name_5 = leader_5[9:-1]

#leader_6 = leader_boards[5]
#leader_score_6 = leader_6[0:9]
#leader_name_6 = leader_6[9:-1]

#leader_7 = leader_boards[6]
#leader_score_7 = leader_7[0:9]
#leader_name_7 = leader_7[9:-1]

#leader_8 = leader_boards[7]
#leader_score_8 = leader_8[0:9]
#leader_name_8 = leader_8[9:-1]

#leader_9 = leader_boards[8]
#leader_score_9 = leader_9[0:9]
#leader_name_9 = leader_9[9:-1]

#leader_10 = leader_boards[9]
#leader_score_10 = leader_10[0:9]
#leader_name_10 = leader_10[9:-1]


# Run until the user asks to quit
running = True
while running:
    # Timer to set score and astroid difficulty
    total_time = round((time.time() - start_time), 2)

    pygame.time.delay(difficulty)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if lives < 1:
        game_over = True

    # Score by time

    if total_time > score_time:
        score_time = total_time + 10
        if total_time < 15:
            score += 100
        elif total_time < 25:
            score += 300
        elif total_time < 40:
            score += 500

    if game_over:
        vel_x = 0
        vel_y = 0
        draws = 165
        draw = 250
        game = 110
        game_1 = 300
        score_time = 0
        total_time = 0
        if new_score:
            score_writer = open("Hi_Scores.txt", 'w')
            #score_writer.write("1. " + str(hi))
            score_writer.close()
    else:
        draws = -250
        draw = -250
        game = -250
        game_1 = -250

    y += vel_y  # This line is the acceleration plus the vel added to y
    x += vel_x  # This line is the acceleration plus the vel added to x
    if -5 > y or y > 450 and bounce_y:  # This controls what happens when the ship hits the wall
        if y < 0:
            y = 1
        else:
            y = 460
        vel_y /= 2
        vel_y *= -1
        bounce_y = False
    if 500 - 50 > y > 0:
        bounce_y = True

    # Astroid Logic
    if 3 < total_time < 90000:
        for i in range(3):
            spot_pick = random.randint(0, 9)
            spot_pick_1 = random.randint(0, 9)
            spot_pick_2 = random.randint(0, 9)
            spot_pick_3 = random.randint(0, 9)
        if not as_move:
            if spot_pick == 0:
                ax_1 = pos_1[0]
                ay_1 = pos_1[1]
                as_move = True
                x_move_pos = True
                y_move_pos = True
            elif spot_pick == 1:
                ax_1 = pos_2[0]
                ay_1 = pos_2[1]
                as_move = True
                x_move_pos = True
                y_move_pos = True
            elif spot_pick == 2:
                ax_1 = pos_3[0]
                ay_1 = pos_3[1]
                as_move = True
                x_move_pos = True
                y_move_pos = True
            elif spot_pick == 3:
                ax_1 = pos_4[0]
                ay_1 = pos_4[1]
                as_move = True
                x_move_pos = True
                y_move_pos = True
            elif spot_pick == 4:
                ax_1 = pos_5[0]
                ay_1 = pos_5[1]
                as_move = True
                x_move_pos = False
                y_move_pos = True
            elif spot_pick == 5:
                ax_1 = pos_6[0]
                ay_1 = pos_6[1]
                as_move = True
                x_move_pos = False
                y_move_pos = True
            elif spot_pick == 6:
                ax_1 = pos_7[0]
                ay_1 = pos_7[1]
                x_move_pos = False
                y_move_pos = True
                as_move = True
            elif spot_pick == 7:
                ax_1 = pos_8[0]
                ay_1 = pos_8[1]
                as_move = True
                x_move_pos = True
                y_move_pos = False
            elif spot_pick == 8:
                ax_1 = pos_9[0]
                ay_1 = pos_9[1]
                as_move = True
                x_move_pos = False
                y_move_pos = False
            elif spot_pick == 9:
                ax_1 = pos_10[0]
                ay_1 = pos_10[1]
                as_move = True
                x_move_pos = False
                y_move_pos = False

        #

        if not as_move_2:
            if spot_pick_1 == 0:
                ax_2 = pos_1[0]
                ay_2 = pos_1[1]
                as_move_2 = True
                x_move_pos_1 = True
                y_move_pos_1 = True
            elif spot_pick_1 == 1:
                ax_2 = pos_2[0]
                ay_2 = pos_2[1]
                as_move_2 = True
                x_move_pos_1 = True
                y_move_pos_1 = True
            elif spot_pick_1 == 2:
                ax_2 = pos_3[0]
                ay_2 = pos_3[1]
                as_move_2 = True
                x_move_pos_1 = True
                y_move_pos_1 = True
            elif spot_pick_1 == 3:
                ax_2 = pos_4[0]
                ay_2 = pos_4[1]
                as_move_2 = True
                x_move_pos_1 = True
                y_move_pos_1 = True
            elif spot_pick_1 == 4:
                ax_2 = pos_5[0]
                ay_2 = pos_5[1]
                as_move_2 = True
                x_move_pos_1 = False
                y_move_pos_1 = True
            elif spot_pick_1 == 5:
                ax_2 = pos_6[0]
                ay_2 = pos_6[1]
                as_move_2 = True
                x_move_pos_1 = False
                y_move_pos_1 = True
            elif spot_pick_1 == 6:
                ax_2 = pos_7[0]
                ay_2 = pos_7[1]
                x_move_pos_1 = False
                y_move_pos_1 = True
                as_move_2 = True
            elif spot_pick_1 == 7:
                ax_2 = pos_8[0]
                ay_2 = pos_8[1]
                as_move_2 = True
                x_move_pos_1 = True
                y_move_pos_1 = False
            elif spot_pick_1 == 8:
                ax_2 = pos_9[0]
                ay_2 = pos_9[1]
                as_move_2 = True
                x_move_pos_1 = False
                y_move_pos_1 = False
            elif spot_pick_1 == 9:
                ax_2 = pos_10[0]
                ay_2 = pos_10[1]
                as_move_2 = True
                x_move_pos_1 = False
                y_move_pos_1 = False
        if not as_move_3:
            if spot_pick_2 == 0:
                ax_3 = pos_1[0]
                ay_3 = pos_1[1]
                as_move_3 = True
                x_move_pos_2 = True
                y_move_pos_2 = True
            elif spot_pick_2 == 1:
                ax_3 = pos_2[0]
                ay_3 = pos_2[1]
                as_move_3 = True
                x_move_pos_2 = True
                y_move_pos_2 = True
            elif spot_pick_2 == 2:
                ax_3 = pos_3[0]
                ay_3 = pos_3[1]
                as_move_3 = True
                x_move_pos_2 = True
                y_move_pos_2 = True
            elif spot_pick_2 == 3:
                ax_3 = pos_4[0]
                ay_3 = pos_4[1]
                as_move_3 = True
                x_move_pos_2 = True
                y_move_pos_2 = True
            elif spot_pick_2 == 4:
                ax_3 = pos_5[0]
                ay_3 = pos_5[1]
                as_move_3 = True
                x_move_pos_2 = False
                y_move_pos_2 = True
            elif spot_pick_2 == 5:
                ax_3 = pos_6[0]
                ay_3 = pos_6[1]
                as_move_3 = True
                x_move_pos_2 = False
                y_move_pos_2 = True
            elif spot_pick_2 == 6:
                ax_3 = pos_7[0]
                ay_3 = pos_7[1]
                x_move_pos_2 = False
                y_move_pos_2 = True
                as_move_3 = True
            elif spot_pick_2 == 7:
                ax_3 = pos_8[0]
                ay_3 = pos_8[1]
                as_move_3 = True
                x_move_pos_2 = True
                y_move_pos_2 = False
            elif spot_pick_2 == 8:
                ax_3 = pos_9[0]
                ay_3 = pos_9[1]
                as_move_3 = True
                x_move_pos_2 = False
                y_move_pos_2 = False
            elif spot_pick_2 == 9:
                ax_3 = pos_10[0]
                ay_3 = pos_10[1]
                as_move_3 = True
                x_move_pos_2 = False
                y_move_pos_2 = False
        if not as_move_4:
            if spot_pick_3 == 0:
                ax_4 = pos_1[0]
                ay_4 = pos_1[1]
                as_move_4 = True
                x_move_pos_3 = True
                y_move_pos_3 = True
            elif spot_pick_3 == 1:
                ax_4 = pos_2[0]
                ay_4 = pos_2[1]
                as_move_4 = True
                x_move_pos_3 = True
                y_move_pos_3 = True
            elif spot_pick_3 == 2:
                ax_4 = pos_3[0]
                ay_4 = pos_3[1]
                as_move_4 = True
                x_move_pos_3 = True
                y_move_pos_3 = True
            elif spot_pick_3 == 3:
                ax_4 = pos_4[0]
                ay_4 = pos_4[1]
                as_move_4 = True
                x_move_pos_3 = True
                y_move_pos_3 = True
            elif spot_pick_3 == 4:
                ax_4 = pos_5[0]
                ay_4 = pos_5[1]
                as_move_4 = True
                x_move_pos_3 = False
                y_move_pos_3 = True
            elif spot_pick_3 == 5:
                ax_4 = pos_6[0]
                ay_4 = pos_6[1]
                as_move_4 = True
                x_move_pos_3 = False
                y_move_pos_3 = True
            elif spot_pick_3 == 6:
                ax_4 = pos_7[0]
                ay_4 = pos_7[1]
                x_move_pos_3 = False
                y_move_pos_3 = True
                as_move_4 = True
            elif spot_pick_3 == 7:
                ax_4 = pos_8[0]
                ay_4 = pos_8[1]
                as_move_4 = True
                x_move_pos_3 = True
                y_move_pos_3 = False
            elif spot_pick_3 == 8:
                ax_4 = pos_9[0]
                ay_4 = pos_9[1]
                as_move_4 = True
                x_move_pos_3 = False
                y_move_pos_3 = False
            elif spot_pick_3 == 9:
                ax_4 = pos_10[0]
                ay_4 = pos_10[1]
                as_move_4 = True
                x_move_pos_3 = False
                y_move_pos_3 = False

        else:
            if y_move_pos:
                y_mover = random.randint(0, 3)
            else:
                y_mover = random.randint(-3, 0)
            if x_move_pos:
                x_mover = random.randint(0, 3)
            else:
                x_mover = random.randint(-3, 0)

                #

            if y_move_pos_1:
                y_mover_1 = random.randint(0, 3)
            else:
                y_mover_1 = random.randint(-3, 0)
            if x_move_pos_1:
                x_mover_1 = random.randint(0, 3)
            else:
                x_mover_1 = random.randint(-3, 0)

                #

            if y_move_pos_2:
                y_mover_2 = random.randint(0, 3)
            else:
                y_mover_2 = random.randint(-3, 0)
            if x_move_pos_2:
                x_mover_2 = random.randint(0, 3)
            else:
                x_mover_2 = random.randint(-3, 0)

                #

            if y_move_pos_3:
                y_mover_3 = random.randint(0, 3)
            else:
                y_mover_3 = random.randint(-3, 0)
            if x_move_pos_3:
                x_mover_3 = random.randint(0, 3)
            else:
                x_mover_3 = random.randint(-3, 0)

            ax_1 += x_mover
            ay_1 += y_mover

            ax_2 += y_mover_1
            ay_2 += y_mover_1

            ax_3 += y_mover_2
            ay_3 += y_mover_2

            ax_4 += y_mover_3
            ax_4 += y_mover_3

    if ax_1 > 550:
        as_move = False
    if ax_1 < -50:
        as_move = False
    if ay_1 > 500:
        as_move = False
    if ay_1 < -50:
        as_move = False

    if ax_2 > 550:
        as_move_2 = False
    if ax_2 < -50:
        as_move_2 = False
    if ay_2 > 500:
        as_move_2 = False
    if ay_2 < -50:
        as_move_2 = False

    if ax_3 > 550:
        as_move_3 = False
    if ax_3 < -50:
        as_move_3 = False
    if ay_3 > 500:
        as_move_3 = False
    if ay_3 < -50:
        as_move_3 = False

    if ax_4 > 550:
        as_move_4 = False
    if ax_4 < -50:
        as_move_4 = False
    if ay_4 > 500:
        as_move_4 = False
    if ay_4 < -50:
        as_move_4 = False

    if -5 > x or x > 450 and bounce_x:  # This controls what happens when the ship hits the wall
        if x < 0:
            x = 1
        else:
            x = 460
        vel_x /= 2
        vel_x *= -1
        bounce_x = False
    if 500 - 50 > x > 0:
        bounce_x = True

    # User Input
    # Left to right movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and 500 - 50 > x > 0 and not exploded:
        vel_x -= acc
        if not shooting:
            going_left = True
            going_right = False
        else:
            n_going_left = True
            n_going_right = False

    if keys[pygame.K_d] and 0 < x < 500 - 50 and not exploded:
        vel_x += acc

        # Below determines which way the bullet goes
        if not shooting:
            going_right = True
            going_left = False
        else:
            n_going_right = True
            n_going_left = False

    # Up and down movement
    if keys[pygame.K_w] and 500 - 50 > y > 0 and not exploded:
        vel_y -= acc

        if not shooting:
            going_up = True
            going_down = False
        else:
            n_going_up = True
            n_going_down = False

    if keys[pygame.K_s] and 0 < y < 500 - 50:
        vel_y += acc
        shipps = ship_dd
        if not shooting:
            going_down = True
            going_up = False
        else:
            n_going_down = True
    else:
        going_down = False
        n_going_down = False

    # Menu Controls
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        if not started:
            if menu_pos <= 3:
                menu_pos += 1

    if keys[pygame.K_w] or keys[pygame.K_UP]:
        if not started:
            if menu_pos >= 1:
                menu_pos -= 1
    if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
        if not started:
            if menu_pos == 1:
                started = True
            elif menu_pos == 2:
                in_leader_board = True
            elif menu_pos == 3:
                running = False

    if menu_pos < 1:
        menu_pos = 1
    elif menu_pos > 3:
        menu_pos = 3

    # Controls which sprite based on direction and speed
    if keys[pygame.K_d] and keys[pygame.K_w] and not exploded:
        shipps = ship_u_r
        direct = 'u_r'  # Used to tell which way the bullet should fire. In this case up and right
    elif keys[pygame.K_d] and keys[pygame.K_s] and not exploded:
        shipps = ship_d_r
        direct = 'd_r'
    elif keys[pygame.K_a] and keys[pygame.K_w] and not exploded:
        shipps = ship_u_l
        direct = 'u_l'
    elif keys[pygame.K_a] and keys[pygame.K_s] and not exploded:
        shipps = ship_d_l
        direct = 'd_l'
    elif keys[pygame.K_s] and not exploded:
        shipps = ship_dd
        direct = 'dd'
    elif keys[pygame.K_w] and not exploded:
        shipps = ship_u_u_r
        direct = 'uu'
    elif keys[pygame.K_d] and not exploded:
        shipps = ship
        direct = 'rr'
    elif keys[pygame.K_a] and not exploded:
        shipps = ship_l
        direct = 'll'

    # Shooting logic
    if keys[pygame.K_SPACE]:
        if not shooting and not exploded:
            shooting = True
            shoot_x = x + 15
            shoot_y = y + 10
        if game_over:
            pygame.time.delay(500)
            lives = 5
            game_over = False
            score = 0
            ship_1 = 450
            ship_2 = 450
            ship_3 = 450
            ship_4 = 450

    if 510 > shoot_x > -10 and shooting and -10 < shoot_y < 510:
        if shoot_x == x + 15:
            if direct == 'u_r':
                shoot_x += shoot_vel
                shoot_y -= shoot_vel
                bul_going = 1
            elif direct == 'd_r':
                shoot_x += shoot_vel
                shoot_y += shoot_vel
                bul_going = 2
            elif direct == 'u_l':
                shoot_y -= shoot_vel
                shoot_x -= shoot_vel
                bul_going = 3
            elif direct == 'd_l':
                shoot_y += shoot_vel
                shoot_x -= shoot_vel
                bul_going = 4
            elif direct == 'dd':
                shoot_y += shoot_vel
                bul_going = 5
            elif direct == 'uu':
                shoot_y -= shoot_vel
                bul_going = 6
            elif direct == 'rr':
                shoot_x += shoot_vel
                bul_going = 7
            elif direct == 'll':
                shoot_x -= shoot_vel
                bul_going = 8
        else:
            if bul_going == 1:
                shoot_x += shoot_vel
                shoot_y -= shoot_vel
            elif bul_going == 2:
                shoot_x += shoot_vel
                shoot_y += shoot_vel
            elif bul_going == 3:
                shoot_y -= shoot_vel
                shoot_x -= shoot_vel
            elif bul_going == 4:
                shoot_y += shoot_vel
                shoot_x -= shoot_vel
            elif bul_going == 5:
                shoot_y += shoot_vel
            elif bul_going == 6:
                shoot_y -= shoot_vel
            elif bul_going == 7:
                shoot_x += shoot_vel
            elif bul_going == 8:
                shoot_x -= shoot_vel
    else:
        shooting = False
        shoot_x = -100

    # if sass_moving:
    #     ax_5 += sass_mover_x
    #     ax_9 += sass_mover_x
    #     ay_5 += sass_mover_y
    #     ay_9 += sass_mover_y
    # if sass_moving_1:
    #     ax_6 += sass_mover_x_1
    #     ax_10 += sass_mover_x_1
    #     ay_6 += sass_mover_y_1
    #     ay_10 += sass_mover_y_1
    # if sass_moving_2:
    #     ax_7 += sass_mover_x_2
    #     ax_11 += sass_mover_x_2
    #     ay_7 += sass_mover_y_2
    #     ay_11 += sass_mover_y_2
    # if sass_moving_3:
    #     ax_8 += sass_mover_x_3
    #     ax_12 += sass_mover_x_3
    #     ay_8 += sass_mover_y_3
    #     ay_12 += sass_mover_y_3

    # Collision Logic

    shipp_hb = [x, x + 50, y, y + 50]

    bass_1_hb = [ax_1, ax_1 + 50, ay_1, ay_1 + 50]
    bass_2_hb = [ax_2, ax_2 + 50, ay_2, ay_2 + 50]
    bass_3_hb = [ax_3, ax_3 + 50, ay_3, ay_3 + 50]
    bass_4_hb = [ax_4, ax_4 + 50, ay_4, ay_4 + 50]

    # sass_1_hb = [ax_5, ax_5 + 10, ay_5, ay_5 + 10]
    # sass_2_hb = [ax_6, ax_6 + 12, ay_6, ay_6 + 10]
    # sass_3_hb = [ax_7, ax_7 + 12, ay_7, ay_7 + 10]
    # sass_4_hb = [ax_8, ax_8 + 15, ay_8, ay_8 + 11]
    # sass_5_hb = [ax_9, ax_9 + 10, ay_9, ay_9 + 10]
    # sass_6_hb = [ax_10, ax_10 + 12, ay_10, ay_10 + 10]
    # sass_7_hb = [ax_11, ax_11 + 12, ay_11, ay_11 + 10]
    # sass_8_hb = [ax_12, ax_12 + 12, ay_12, ay_12 + 10]

    shoot_hb = [shoot_x, shoot_x + 10, shoot_y, shoot_y + 5]

    if exploded:
        x = x_1
        y = y_1
        as_move = False
        as_move_2 = False
        as_move_3 = False
        as_move_4 = False
        shipps = explosion

    if total_time - new_time >= 1 and exploded:
        x = 50
        y = 50
        vel_y = 0
        vel_x = 0
        exploded = False
        shipps = ship

    # if sass_1_hb[0] <= shipp_hb[0] <= sass_1_hb[1] or sass_1_hb[0] <= shipp_hb[1] <= sass_1_hb[1]:
    #     if sass_1_hb[2] <= shipp_hb[2] <= sass_1_hb[3] or sass_1_hb[2] <= shipp_hb[3] <= sass_1_hb[3]:
    #         lives -= 1
    #         as_move = False
    #         new_time = total_time
    #         exploded = True
    #         x_1 = x
    #         y_1 = y
#
    # if sass_2_hb[0] <= shipp_hb[0] <= sass_2_hb[1] or sass_2_hb[0] <= shipp_hb[1] <= sass_2_hb[1]:
    #     if sass_2_hb[2] <= shipp_hb[2] <= sass_2_hb[3] or sass_2_hb[2] <= shipp_hb[3] <= sass_2_hb[3]:
    #         lives -= 1
    #         as_move_2 = False
    #         new_time = total_time
    #         exploded = True
    #         x_1 = x
    #         y_1 = y
#
    # if sass_3_hb[0] <= shipp_hb[0] <= sass_3_hb[1] or sass_3_hb[0] <= shipp_hb[1] <= sass_3_hb[1]:
    #     if sass_3_hb[2] <= shipp_hb[2] <= sass_3_hb[3] or sass_3_hb[2] <= shipp_hb[3] <= sass_3_hb[3]:
    #         lives -= 1
    #         as_move_2 = False
    #         new_time = total_time
    #         exploded = True
    #         x_1 = x
    #         y_1 = y
#
    # if sass_4_hb[0] <= shipp_hb[0] <= sass_4_hb[1] or sass_4_hb[0] <= shipp_hb[1] <= sass_4_hb[1]:
    #     if sass_4_hb[2] <= shipp_hb[2] <= sass_4_hb[3] or sass_4_hb[2] <= shipp_hb[3] <= sass_4_hb[3]:
    #         lives -= 1
    #         as_move_2 = False
    #         new_time = total_time
    #         exploded = True
    #         x_1 = x
    #         y_1 = y
#
    # if sass_5_hb[0] <= shipp_hb[0] <= sass_5_hb[1] or sass_5_hb[0] <= shipp_hb[1] <= sass_5_hb[1]:
    #     if sass_5_hb[2] <= shipp_hb[2] <= sass_5_hb[3] or sass_5_hb[2] <= shipp_hb[3] <= sass_5_hb[3]:
    #         lives -= 1
    #         as_move_2 = False
    #         new_time = total_time
    #         exploded = True
    #         x_1 = x
    #         y_1 = y
#
    # if sass_6_hb[0] <= shipp_hb[0] <= sass_6_hb[1] or sass_6_hb[0] <= shipp_hb[1] <= sass_6_hb[1]:
    #     if sass_6_hb[2] <= shipp_hb[2] <= sass_6_hb[3] or sass_6_hb[2] <= shipp_hb[3] <= sass_6_hb[3]:
    #         lives -= 1
    #         as_move_2 = False
    #         new_time = total_time
    #         exploded = True
    #         x_1 = x
    #         y_1 = y
#
    # if sass_7_hb[0] <= shipp_hb[0] <= sass_7_hb[1] or sass_7_hb[0] <= shipp_hb[1] <= sass_7_hb[1]:
    #     if sass_7_hb[2] <= shipp_hb[2] <= sass_7_hb[3] or sass_7_hb[2] <= shipp_hb[3] <= sass_7_hb[3]:
    #         lives -= 1
    #         as_move_2 = False
    #         new_time = total_time
    #         exploded = True
    #         x_1 = x
    #         y_1 = y
#
    # if sass_8_hb[0] <= shipp_hb[0] <= sass_8_hb[1] or sass_8_hb[0] <= shipp_hb[1] <= sass_8_hb[1]:
    #     if sass_8_hb[2] <= shipp_hb[2] <= sass_8_hb[3] or sass_8_hb[2] <= shipp_hb[3] <= sass_8_hb[3]:
    #         lives -= 1
    #         as_move_2 = False
    #         new_time = total_time
    #         exploded = True
    #         x_1 = x
    #         y_1 = y

    #

    if bass_1_hb[0] <= shipp_hb[0] <= bass_1_hb[1] or bass_1_hb[0] <= shipp_hb[1] <= bass_1_hb[1]:
        if bass_1_hb[2] <= shipp_hb[2] <= bass_1_hb[3] or bass_1_hb[2] <= shipp_hb[3] <= bass_1_hb[3]:
            lives -= 1
            as_move = False
            new_time = total_time
            exploded = True
            x_1 = x
            y_1 = y

    if bass_2_hb[0] <= shipp_hb[0] <= bass_2_hb[1] or bass_2_hb[0] <= shipp_hb[1] <= bass_2_hb[1]:
        if bass_2_hb[2] <= shipp_hb[2] <= bass_2_hb[3] or bass_2_hb[2] <= shipp_hb[3] <= bass_2_hb[3]:
            lives -= 1
            as_move_2 = False
            new_time = total_time
            exploded = True
            x_1 = x
            y_1 = y

    if bass_3_hb[0] <= shipp_hb[0] <= bass_3_hb[1] or bass_3_hb[0] <= shipp_hb[1] <= bass_3_hb[1]:
        if bass_3_hb[2] <= shipp_hb[2] <= bass_3_hb[3] or bass_3_hb[2] <= shipp_hb[3] <= bass_3_hb[3]:
            lives -= 1
            as_move_3 = False
            new_time = total_time
            exploded = True
            x_1 = x
            y_1 = y

    if bass_4_hb[0] <= shipp_hb[0] <= bass_4_hb[1] or bass_4_hb[0] <= shipp_hb[1] <= bass_4_hb[1]:
        if bass_4_hb[2] <= shipp_hb[2] <= bass_4_hb[3] or bass_4_hb[2] <= shipp_hb[3] <= bass_4_hb[3]:
            lives -= 1
            as_move_4 = False
            new_time = total_time
            exploded = True
            x_1 = x
            y_1 = y

    # Bullet Collision

    # if sass_1_hb[0] <= shoot_hb[0] <= sass_1_hb[1] or sass_1_hb[0] <= shoot_hb[1] <= sass_1_hb[1]:
    #     if sass_1_hb[2] <= shoot_hb[2] <= sass_1_hb[3] or sass_1_hb[2] <= shoot_hb[3] <= sass_1_hb[3]:
    #         ax_5 = -250
    #         score += 75
#
    # if sass_2_hb[0] <= shoot_hb[0] <= sass_2_hb[1] or sass_2_hb[0] <= shoot_hb[1] <= sass_2_hb[1]:
    #     if sass_2_hb[2] <= shoot_hb[2] <= sass_2_hb[3] or sass_2_hb[2] <= shoot_hb[3] <= sass_2_hb[3]:
    #         ax_6 = -250
    #         score += 75
#
    # if sass_3_hb[0] <= shoot_hb[0] <= sass_3_hb[1] or sass_3_hb[0] <= shoot_hb[1] <= sass_3_hb[1]:
    #     if sass_3_hb[2] <= shoot_hb[2] <= sass_3_hb[3] or sass_3_hb[2] <= shoot_hb[3] <= sass_3_hb[3]:
    #         ax_7 = -250
    #         score += 75
#
    # if sass_4_hb[0] <= shoot_hb[0] <= sass_4_hb[1] or sass_4_hb[0] <= shoot_hb[1] <= sass_4_hb[1]:
    #     if sass_4_hb[2] <= shoot_hb[2] <= sass_4_hb[3] or sass_4_hb[2] <= shoot_hb[3] <= sass_4_hb[3]:
    #         ax_8 = -250
    #         score += 75
#
    # if sass_5_hb[0] <= shoot_hb[0] <= sass_5_hb[1] or sass_5_hb[0] <= shoot_hb[1] <= sass_5_hb[1]:
    #     if sass_5_hb[2] <= shoot_hb[2] <= sass_5_hb[3] or sass_5_hb[2] <= shoot_hb[3] <= sass_5_hb[3]:
    #         ax_9 = -250
    #         score += 75
#
    # if sass_6_hb[0] <= shoot_hb[0] <= sass_6_hb[1] or sass_6_hb[0] <= shoot_hb[1] <= sass_6_hb[1]:
    #     if sass_6_hb[2] <= shoot_hb[2] <= sass_6_hb[3] or sass_6_hb[2] <= shoot_hb[3] <= sass_6_hb[3]:
    #         ax_10 = -250
    #         score += 75
#
    # if sass_7_hb[0] <= shoot_hb[0] <= sass_7_hb[1] or sass_7_hb[0] <= shoot_hb[1] <= sass_7_hb[1]:
    #     if sass_7_hb[2] <= shoot_hb[2] <= sass_7_hb[3] or sass_7_hb[2] <= shoot_hb[3] <= sass_7_hb[3]:
    #         ax_11 = -250
    #         score += 75
#
    # if sass_8_hb[0] <= shoot_hb[0] <= sass_8_hb[1] or sass_8_hb[0] <= shoot_hb[1] <= sass_8_hb[1]:
    #     if sass_8_hb[2] <= shoot_hb[2] <= sass_8_hb[3] or sass_8_hb[2] <= shoot_hb[3] <= sass_8_hb[3]:
    #         ax_12 = -250
    #         score += 75
#
    # #

    if bass_1_hb[0] <= shoot_hb[0] <= bass_1_hb[1] or bass_1_hb[0] <= shoot_hb[1] <= bass_1_hb[1]:
        if bass_1_hb[2] <= shoot_hb[2] <= bass_1_hb[3] or bass_1_hb[2] <= shoot_hb[3] <= bass_1_hb[3]:
            sass_mover_y = y_mover
            sass_mover_x = x_mover
            sass_moving = True
            ax_5 = ax_1
            ax_9 = ax_1
            ax_1 = -250
            score += 250

    if bass_2_hb[0] <= shoot_hb[0] <= bass_2_hb[1] or bass_2_hb[0] <= shoot_hb[1] <= bass_2_hb[1]:
        if bass_2_hb[2] <= shoot_hb[2] <= bass_2_hb[3] or bass_2_hb[2] <= shoot_hb[3] <= bass_2_hb[3]:
            sass_mover_y_1 = y_mover_1
            sass_mover_x_1 = x_mover_1
            sass_moving_1 = True
            ax_6 = ax_2
            ax_10 = ax_2
            ax_2 = -250
            score += 250

    if bass_3_hb[0] <= shoot_hb[0] <= bass_3_hb[1] or bass_3_hb[0] <= shoot_hb[1] <= bass_3_hb[1]:
        if bass_3_hb[2] <= shoot_hb[2] <= bass_3_hb[3] or bass_3_hb[2] <= shoot_hb[3] <= bass_3_hb[3]:
            sass_moving_2 = True
            sass_mover_y_2 = y_mover_2
            sass_mover_x_2 = x_mover_2
            ax_7 = ax_3
            ax_11 = ax_3
            ax_3 = -250
            score += 250

    if bass_4_hb[0] <= shoot_hb[0] <= bass_4_hb[1] or bass_4_hb[0] <= shoot_hb[1] <= bass_4_hb[1]:
        if bass_4_hb[2] <= shoot_hb[2] <= bass_4_hb[3] or bass_4_hb[2] <= shoot_hb[3] <= bass_4_hb[3]:
            sass_moving_3 = True
            sass_mover_y_3 = y_mover_3
            sass_mover_x_3 = x_mover_3
            ax_8 = ax_4
            ax_12 = ax_4
            ax_4 = -250
            score += 250

    if score > 1:
        pass

    if lives == 4:
        ship_1 = 550
    elif lives == 3:
        ship_1 = 550
        ship_2 = 550
    elif lives == 2:
        ship_1 = 550
        ship_2 = 550
        ship_3 = 550
    elif lives == 1:
        ship_1 = 550
        ship_2 = 550
        ship_3 = 550
        ship_4 = 550

    # Background
    win.fill((0, 0, 0))

    font = pygame.font.SysFont(None, 40)
    img = font.render('GAME OVER', True, (255, 255, 0))
    game_o = font.render('Press Space to Restart', True, (255, 255, 0))
    lives_count = font.render((str(lives)), True, (255, 255, 0))
    scoreboard = font.render((str(score)), True, (255, 255, 0))
    score_thingy = font.render('Score: ', True, (255, 255, 0))
    high = font.render('Hi:', True, (255, 255, 0))
    # hi_score = font.render(str(hi), True, (255, 255, 0))
    start = font.render('START', True, (0, 0, 255))
    leader_board = font.render('LEADERBOARD', True, (0, 0, 255))
    exit_game = font.render('EXIT', True, (0, 0, 255))

    if started and not in_leader_board:
        pygame.draw.rect(win, (255, 255, 0), (60, 15, 400, 60), 2)
        pygame.draw.line(win, (255, 255, 0), (270, 15), (270, 73))

        pygame.draw.rect(win, (255, 255, 0), (60, 15, 400, 60), 2)
        pygame.draw.line(win, (255, 255, 0), (270, 15), (270, 73))

        # win.blit(hi_score, (330, 30))
        win.blit(high, (285, 30))
        win.blit(img, (draws, draw))
        win.blit(game_o, (game, game_1))
        win.blit(scoreboard, (160, 30))
        win.blit(score_thingy, (70, 30))

        # Geometry
        win.blit(ship_icon, (290, ship_1))
        win.blit(ship_icon, (330, ship_2))
        win.blit(ship_icon, (370, ship_3))
        win.blit(ship_icon, (410, ship_4))
        win.blit(ship_icon, (450, ship_5))

        win.blit(shipps, (x, y))
        pygame.draw.rect(win, (255, 255, 0), (shoot_x, shoot_y + 10, 10, 5))

        # Stroids
        win.blit(crazy_1, (ax_1, ay_1))
        win.blit(crazy_2, (ax_2, ay_2))
        win.blit(crazy_3, (ax_3, ay_3))
        win.blit(crazy_4, (ax_4, ay_4))
        # win.blit(sass_1, (ax_5, ay_5))
        # win.blit(sass_2, (ax_6, ay_6))
        # win.blit(sass_3, (ax_7, ay_7))
        # win.blit(sass_4, (ax_8, ay_8))
        # win.blit(sass_1, (ax_9, ay_9))
        # win.blit(sass_2, (ax_10, ay_10))
        # win.blit(sass_3, (ax_11, ay_11))
        # win.blit(sass_4, (ax_12, ay_12))

    # Text and Such

    elif not in_leader_board:
        pygame.time.delay(40)
        started = False
        if menu_pos == 1:
            pygame.draw.rect(win, (255, 255, 0), (130, 265, 225, 50))
        elif menu_pos == 2:
            pygame.draw.rect(win, (255, 255, 0), (130, 330, 225, 50))
        elif menu_pos == 3:
            pygame.draw.rect(win, (255, 255, 0), (130, 395, 225, 50))

        win.blit(title_screen, (95, 100))
        pygame.draw.rect(win, (255, 255, 0), (130, 265, 225, 50), 2)
        pygame.draw.rect(win, (255, 255, 0), (130, 330, 225, 50), 2)
        pygame.draw.rect(win, (255, 255, 0), (130, 395, 225, 50), 2)
        win.blit(start, (200, 275))
        win.blit(leader_board, (135, 345))
        win.blit(exit_game, (205, 408))

    else:
        for i in range(2874590218375982374658972345087235):
            bruh = None
            if bruh is None:
                print()


    pygame.display.flip()
pygame.quit()
