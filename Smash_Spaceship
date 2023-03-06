import pygame
import random
import time

pygame.font.init()
pygame.mixer.init()

class spaceship:
    def __init__(self, position, color_scheme, control, firing_contr, icon_path, p_icon):
        self.x, self.y = position
        self.color = color_scheme
        self.speed_x = 0
        self.speed_y = 0
        self.speed_const = 0.4
        self.controls = control
        self.fire = firing_contr
        self.health = 35
        self.bullet_count = 70
        self.icon = pygame.image.load(icon_path)
        self.powerup_icon = p_icon
        return

    def move(self, key):
        if (key == self.controls[0]):
            self.speed_x = -self.speed_const
        if (key == self.controls[1]):
            self.speed_x = self.speed_const
        if (key == self.controls[2]):
            self.speed_y = -self.speed_const
        if (key == self.controls[3]):
            self.speed_y = self.speed_const

        if (key in self.fire):
            dx, dy, dm, imp = self.fire[key]
            ip = "bullet.png" if dm == 1 else "bullets.png"
            if (self.bullet_count >= imp):
                self.bullet_count -= imp
                bullet(dx, dy, self, (self.x, self.y), dm, ip)
        return

    def stop(self, key):
        if (key == self.controls[0]):
            self.speed_x = 0
        elif (key == self.controls[1]):
            self.speed_x = 0
        elif (key == self.controls[2]):
            self.speed_y = 0
        elif (key == self.controls[3]):
            self.speed_y = 0
        return

    def fired(self, i):
        self.health -= i.damage
        if (self.health <= 0):
            game_over()
        bullet.bullets.remove(i)
        return


class bullet:
    bullets = []
    super_sound = pygame.mixer.Sound("Grenade+1.mp3")
    bullet_sound = pygame.mixer.Sound("Gun+Silencer.mp3")
    def __init__(self, dir_x, dir_y, parent, coor, damage, icon_path):
        self.direction_x = dir_x
        self.direction_y = dir_y
        self.parent = parent
        self.speed = 5
        self.x, self.y = coor
        self.bullets.append(self)
        self.damage = damage
        self.icon = pygame.image.load(icon_path)
        self.icon = pygame.transform.rotate(self.icon, 90*(dir_y))
        if(self.damage == 1):
            pygame.mixer.Sound.play(self.bullet_sound)
        else:
            pygame.mixer.Sound.play(self.super_sound)
        return


class powerups:
    p_ls = []

    def __init__(self, parent):
        self.x = random.randint(display["x"]*0.15, display["x"]*0.85)
        self.y = random.randint(display["y"]*0.15, display["y"]*0.85)
        self.ability = random.randint(-3, 3)
        self.parent = parent
        self.icon = pygame.image.load(self.parent.powerup_icon)
        self.p_ls.append(self)
        return

    def taken(self, claimer):
        p_t = score_f.render(str(self.ability), 1, (40, 50, 0))
        screen.blit(p_t, (self.x, self.y))
        self.parent.health = self.parent.health + self.ability
        p1 = powerups(self.parent)
        self.p_ls.remove(self)
        t = txt(self)
        return


class txt:
    font = pygame.font.SysFont("comicsancs", 48)
    ls = []

    def __init__(self, pwrup):
        self.x = pwrup.x
        self.y = pwrup.y
        self.t = time.time()
        self.color = pwrup.parent.color
        self.parent = pwrup.parent
        self.pwrup = pwrup
        self.ls.append(self)
        self.font = pygame.font.SysFont("comicsancs", 48)

    def print_pwrup_abi(self):
        t = time.time()
        if (t - self.t < 0.5):
            text = self.font.render(
                str(self.pwrup.ability), 1, self.parent.color)
            screen.blit(text, (self.x, self.y))
        else:
            self.ls.remove(self)

# Calculate distance of tuples t1, t2


def dis(t1, t2):
    x1 = t1[0] - t2[0]
    y1 = t1[1] - t2[1]
    d = x1**2 + y1**2
    return d**0.5

# Checks keyboard input as key and assign speed to all characters


def moves(ls, key):
    for i in ls:
        i.move(key)
    return

# Checks keyboard input as key and set speed to 0 for keys released


def stops(ls, key):
    for i in ls:
        i.stop(key)
    return

# Displays all elements/ spirits


def show(ls1, ls2, ls3, l4):
    for i in ls1:
        screen.blit(i.icon, (i.x, i.y))
    for i in ls2:
        screen.blit(i.icon, (i.x, i.y))
    for i in ls3:
        screen.blit(i.icon, (i.x, i.y))
    for i in l4:
        i.print_pwrup_abi()
    return

# Changes coordinates of the spirits


def runs(ls):
    for i in ls:
        i.x = max(min(i.speed_x + i.x, display["x"]*0.95), display["x"]*0.01)
        i.y = max(min(i.speed_y + i.y, display["y"]*0.95), display["y"]*0.01)
    return

# Moves bullets


def shooting(ls):
    for i in ls:
        i.x += i.direction_x * i.speed
        i.y += i.direction_y * i.speed
        for j in players:
            if (i.parent != j):
                if (dis((i.x, i.y), (j.x, j.y)) < 10 + 10*i.damage):
                    j.fired(i)
        if (i.x < 0 or i.x > display["x"]):
            bullet.bullets.remove(i)
    return

# Checks if powerup is taken


def powerup_taken(ls1, ls2):
    for i in ls1:
        for j in ls2:
            if (dis((i.x, i.y), (j.x, j.y)) < 30):
                i.taken(j)
    return

# Game over window


def game_over():
    global playing
    playing = False
    b1 = True
    while b1:
        screen.fill((0, 0, 100))
        for action in pygame.event.get():
            if action.type == pygame.QUIT or action.type == pygame.KEYDOWN:
                b1 = False
                break

        gameover_f = pygame.font.SysFont("comicsancs", 48)
        gameover_t = gameover_f.render(
            "GAME OVER! Press any key to QUIT", 1, (255, 255, 255))
        screen.blit(gameover_t, (display["x"]*0.04, display["y"]*0.15))
        pygame.display.update()
    return


# constants
if (1):
    # SCREEN
    display = {"x": 800, "y": 600}
    background_1 = pygame.image.load("BG-1.jpg")
    background_2 = pygame.image.load("BG-2.jpg")

    # yellow
    coor_yellow = (int(display["x"]*0.15), int(display["y"]*0.5))
    color_yellow = (240, 150, 65)
    control_yellow = [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s]
    fire_yellow = {pygame.K_x: (-1, 0, 1, 1),  # dx, dy, dm, imp
                   pygame.K_c: (1, 0, 1, 1),
                   pygame.K_z: (0, -1, 1, 1),
                   pygame.K_v: (0, 1, 1, 1),
                   pygame.K_f: (-1, 0, 3, 2),
                   pygame.K_g: (1, 0, 3, 2)}

    # red
    coor_red = (int(display["x"]*0.85), int(display["y"]*0.5))
    color_red = (180, 60, 25)
    control_red = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
    fire_red = {pygame.K_LEFTBRACKET: (-1, 0, 1, 1),
                pygame.K_RIGHTBRACKET: (1, 0, 1, 1),
                pygame.K_p:           (0, -1, 1, 1),
                pygame.K_BACKSLASH:   (0, 1, 1, 1),
                pygame.K_0:           (-1, 0, 3, 2),
                pygame.K_MINUS:        (1, 0, 3, 2)}

    # Create spaceships
    yellow_spirit = spaceship(
        coor_yellow, color_yellow, control_yellow, fire_yellow, "ufo-5.png", "star.png")
    red_spirit = spaceship(coor_red, color_red, control_red,
                           fire_red, "ufo-4.png", "star-2.png")
    players = [yellow_spirit, red_spirit]

    # Create powerups
    yellow_star = powerups(yellow_spirit)
    red_star = powerups(red_spirit)

    pygame.init()
    screen = pygame.display.set_mode((display["x"], display["y"]))

    b1 = True
    playing = True
    
while b1:
    screen.blit(background_1, (0, 0))
    for action in pygame.event.get():
        if action.type == pygame.QUIT or action.type == pygame.KEYDOWN:
            b1 = False
    pygame.display.update()

msc = pygame.mixer.music.load("feed-the-machine-classic-arcade-game-116846.mp3")
pygame.mixer.music.play()
while playing:
    screen.blit(background_2, (0, 0))
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            playing = False

        elif action.type == pygame.KEYDOWN:
            moves(players, action.key)

        elif action.type == pygame.KEYUP:
            stops(players, action.key)

    runs(players)
    shooting(bullet.bullets)
    powerup_taken(powerups.p_ls, players)
    show(players, bullet.bullets, powerups.p_ls, txt.ls)
    
    for i in players:
        playing = playing*(i.bullet_count)

    score_f = pygame.font.SysFont("comicsancs", 32)
    
    score_1_t = score_f.render( "Health: " + str(players[0].health), 1, (255, 255, 255))
    screen.blit(score_1_t, (display["x"]*0.04, display["y"]*0.15))
    bullet_1_t = score_f.render("Bullet count: " + str(players[0].bullet_count), 1, (255, 255, 255))
    screen.blit(bullet_1_t, (display["x"]*0.04, display["y"]*0.20))

    score_2_t = score_f.render("Health: " + str(players[1].health), 1, (255, 255, 255))
    screen.blit(score_2_t, (display["x"]*0.76, display["y"]*0.15))
    bullet_2_t = score_f.render("Bullet count: " + str(players[1].bullet_count), 1, (255, 255, 255))
    screen.blit(bullet_2_t, (display["x"]*0.76, display["y"]*0.20))

    pygame.display.update()
