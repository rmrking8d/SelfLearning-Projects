import pygame, sys, random, math, time
pygame.init() 

#Constants/Vars
HEIGHT = 748
WIDTH = 1422
#Colors
WHITE = (255,255,255)
#SetUp
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tile Frenzy")
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

#Classes
class Background():
    def __init__(self):
        self.image = pygame.image.load("AimLab_TileFrenzy/Assets/alabbg1.png").convert_alpha()
    def draw(self, surface):
        surface.fill(WHITE)
        surface.blit(self.image, (0,0))
class Tile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("AimLab_TileFrenzy/Assets/Tile.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.posX = random.randrange(int(WIDTH*.25), int(WIDTH*.75))
        self.posY = random.randrange(int(HEIGHT*.25), int(HEIGHT*.75))
        self.amount = 0
    def spawn(self):
        self.rect = self.image.get_rect()
        self.posX = random.randrange(int(WIDTH*.25), int(WIDTH*.75))
        self.posY = random.randrange(int(HEIGHT*.25), int(HEIGHT*.75))
        self.amount += 1
    def draw(self, surface):
        surface.blit(self.image, (self.posX,self.posY))
class Crosshair((pygame.sprite.Sprite)):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("AimLab_TileFrenzy/Assets/crosshair.png").convert_alpha()
        self.shotsound = pygame.mixer.Sound("/Users/rmrking8d/Documents/VS Code/Self Learning:Projects/AimLab_TileFrenzy/Sounds/P250 single shot sound effect   CSGO SFX.wav")
        self.rect = self.image.get_rect()
    def shot(self):
        self.shotsound.play()
class Score:
    def __init__(self):
        self.points = 0
        self.font = pygame.font.SysFont('monospace', 30, bold = False)
    def increase(self):
        self.points += 100
    def reset(self):
        self.points = 0
    def draw(self, surface):
        lbl = self.font.render("Score: " +str(self.points),1, WHITE)
        surface.blit(lbl,(22,5))
class Collision:
    def tileshot(self,tile,crosshair):
        tile = Tile()
        crosshair = Crosshair()
        return tile.rect.colliderect(crosshair.rect)
class Start:
    def __init__(self):
        self.image = pygame.image.load("AimLab_TileFrenzy/Assets/Startbut.png").convert_alpha()
    def draw(self,surface):
        surface.blit(self.image,(530,400))
class Timer:
    def __init__(self):
        pass
    def draw(self, surface):
        pass
#Main Loop
def main():
    #Objects
    background = Background()
    score = Score()
    crosshair = Crosshair()
    tile = Tile()
    collision = Collision()
    start = Start()
    timer = Timer()

    #MainLoop
    while True:
        background.draw(screen)
        score.draw(screen)
        tile.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #Start Menu
            if event.type == pygame.MOUSEMOTION:
                crosshair.rect.center = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN and collision.tileshot(tile,crosshair):
                crosshair.shot()
                tile.amount -= 1
                score.increase()
                tile.spawn()
        #Crosshair Movement
        screen.blit(crosshair.image, crosshair.rect)

        clock.tick(60)
        pygame.display.update()
main()

