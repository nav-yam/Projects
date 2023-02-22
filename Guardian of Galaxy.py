import pygame 
import random 
import time

def main():        
    pygame.mixer.init()
    class pointer():
        def __init__(self):
            self.icon = pygame.image.load("Resources/crosshair.png")
            self.x = 480
            self.y = 230
            self.speed_x = 0
            self.speed_y = 0
            self.speed_const = 0.14
            self.size = 25
            
        def display(self):
            screen.blit(self.icon, (self.x, self.y))
        
        def fire(self, ls, Score):
            for ele in ls:
                d = ele.dis(self) 
                if(d < self.size):
                    ls.remove(ele)
                    Planet_died.play()
                    Score+=1
                    break
            else:
                Score -= 1
                BULLET_FIRE_SOUND.play()
            return Score
            
                    
        
        def set_coor(self, tupl):
            self.x, self.y = tupl
            return
        
        def set_size(self, n):
            self.size = n
        
        
    class enemy():
        k = 5
        Spawn = True
        def __init__(self):
            self.icon = pygame.image.load(enemy_icons[random.randint(0, len(enemy_icons) - 1)])
            self.x = random.randint(40, 830)
            self.y = random.randint(40, 430)
            # j = 
            self.t1 = time.time()
            # print(self.t1)
            self.b = True
            self.emer = True
            
        def display(self):
            screen.blit(self.icon, (self.x, self.y))
            
        def dis(self, Pntr):
            x = self.x - Pntr.x
            y = self.y - Pntr.y 
            dst = x**2 + y**2
            return dst**0.5
        
        def Check_time(self, t3):
            if(t3 - self.t1 > 12 ):
                return False
            elif(t3 - self.t1 > 11.8 ):
                self.icon = pygame.image.load("Resources/blast.png")
                Game_over.play()
            elif(t3 - self.t1 > 7 ):
                Emergency.play()
                if(self.b):
                    self.x += enemy.k
                    self.b = False
                else:
                    self.x -= enemy.k
                    self.b = True
            return True

    if(1):        
        pygame.init()
        screen = pygame.display.set_mode((900, 500))
        pygame.display.set_caption("Guardian of Galaxy", "Icon")
        enemy_icons = ["Resources/asteroid-2.png", "Resources/alien.png", "Resources/meteorite.png", "Resources/rock.png"]

        Pointer = pointer()

        Enemies = []
        e1 = enemy()
        Enemies.append(e1)
        e2 = enemy()
        Enemies.append(e2)

        fire_actions = [pygame.K_KP_ENTER, pygame.K_RETURN, pygame.K_SPACE]

        icon = pygame.image.load("Resources/jupiter.png")
        pygame.display.set_icon(icon)
        back = pygame.image.load("Resources/gradient-galaxy-background_23-2148983655-2.jpg")
        brighten = 64
        back.fill((brighten, brighten, brighten), special_flags=pygame.BLEND_RGB_ADD)

        ls = ["FIRE SIZE INCREASED", "SPAWNING PAUSED", "GROUND CLEARED"]

        t1 = time.time()
        t3 = time.time()
        running = True
        spawn_time = 0.5
        powerup_time = 6
        n = 1
        b_powerup = False
        power_taken = False
        
        BULLET_FIRE_SOUND = pygame.mixer.Sound('Resources/shotgun-firing-4-6746.mp3')
        Planet_died = pygame.mixer.Sound("Resources/hit-sound-effect-12445.mp3")
        Game_over = pygame.mixer.Sound("Resources/explosion-6801.mp3")
        Emergency = pygame.mixer.Sound("Resources/alarm-loop-sound-effect-94369.mp3")
        
        Score = 0
        b1 = True
            
    while running:
        # screen.fill((15, 25, 59))
        screen.blit(back,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                b1 = False
                
            elif event.type == pygame.KEYDOWN:
                if(event.key in fire_actions):
                    Score = Pointer.fire(Enemies, Score)
                    
                    if(b_powerup):
                        x = Pointer.x - powerup_coor[0]
                        y = Pointer.y - powerup_coor[1]
                        dst = x**2 + y**2
                        if(dst**0.5 < 25 and not power_taken):
                            power_taken = True
                            t_powerup_begin = time.time()
                            
                            if(power_num == 0):
                                Pointer.set_size(75)
                            elif(power_num == 1):
                                enemy.Spawn = False
                                #stop spawing
                            elif(power_num == 2):
                                Score += len(Enemies)
                                Enemies.clear()
                            b_powerup = False
                            
                
        coordinates = pygame.mouse.get_pos()
        Pointer.set_coor(coordinates)
        
        pygame.mouse.set_visible(False)
        t2 = time.time()
        t = t2 - t1
        if(t > spawn_time and enemy.Spawn):
            t1 = t2
            Enemies.append(0)
            e1 = enemy()
            Enemies[-1] = e1
        
        if(t2 - t3 > powerup_time*n ):
            power_num = random.randint(0,2)
            ic = pygame.image.load("Resources/ufo.png")
            powerup_coor = (random.randint(40, 850), random.randint(40, 450) )
            screen.blit(ic, powerup_coor)
            n += 1
            b_powerup = True
            power_taken = False
        
        if(b_powerup and not power_taken):
            screen.blit(ic, powerup_coor)
            
        if(power_taken):
            powerup_font = pygame.font.SysFont("comicsans",40)
            powerup_text = powerup_font.render(ls[power_num] ,1,(0,0,0))
            screen.blit(powerup_text,(250,400))
            if(t2 - t_powerup_begin > 3):
                if(power_num == 0):
                    Pointer.set_size(25)
                    print(Pointer.size)
                elif(power_num == 1):
                    enemy.Spawn = True
                    print(enemy.Spawn)
                power_taken = False
            
        if(len(Enemies) > 12):
            running = False
            
        for i in Enemies:
            running = running and i.Check_time(t2)
            # if(not running):
            #     print(i, len(Enemies))
            i.display()    
        score_font = pygame.font.SysFont("comicsans",40)
        score_text = score_font.render("Score : "+str(Score) ,1,(255,255,255))
        screen.blit(score_text,(10,10))
        Pointer.display()
        pygame.display.update()
        
    while b1:
        screen.fill((200, 200, 200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                b1 = False
            elif event.type == pygame.KEYDOWN:
                b1 = False
            
        gameover_font = pygame.font.SysFont("comicsans",60)
        gameover_text = gameover_font.render("! GAME OVER !" ,1,(255,0,0))
        screen.blit(gameover_text,(250,150))
        exit_font = pygame.font.SysFont("comicsans",40)
        exit_text = exit_font.render("Press any key to EXIT", 1, (100, 100, 100))
        screen.blit(exit_text,(250,400))
        pygame.display.update()
        


if __name__ == "__main__":
    main()