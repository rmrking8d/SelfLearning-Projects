import pygame, sys, random, math 
#Constants
HEIGHT = 640
WIDTH = 640
PIXELS = 32
SQUARES = int(WIDTH/PIXELS)

#Colors
BG1 = (156,210,54)
BG2 = (147,203,57)
RED = (255,0,0)
PURP = (46, 37, 168)
BLACK = (0,0,0)

#Class
class Background:
    def draw(self, surface):
        surface.fill(BG1)
        counter = 0 #when to paint a square the second color
        for row in range(SQUARES):
            for col in range(SQUARES):
                if counter % 2 == 0:
                    pygame.draw.rect(surface, BG2, (col * PIXELS, row * PIXELS, PIXELS, PIXELS))
                if col == SQUARES - 1:
                    continue    
                counter += 1
class Apple:
    def __init__(self): #init: constructor method - create our object. Self parameter allows us to access the attributes and methods of the class in python.
        self.color = RED
        self.spawn()

    def spawn(self):
        self.posX = random.randrange(0, WIDTH, PIXELS)
        self.posY = random.randrange(0, HEIGHT, PIXELS)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.posX, self.posY, PIXELS, PIXELS))
class Snake:
    def __init__(self):
        self.color = PURP
        self.headX = random.randrange(0, WIDTH, PIXELS)
        self.headY = random.randrange(0, HEIGHT, PIXELS)
        self.state = "STOP" #var can either be STOP, UP, DOWN, RIGHT, OR LEFT
        self.bodies = []
        self.body_color = 20
    
    def move_head(self):
        if self.state == "UP":
            self.headY -= PIXELS
        elif self.state == "DOWN":
            self.headY += PIXELS
        elif self.state == "RIGHT":
            self.headX += PIXELS
        elif self.state == "LEFT":
            self.headX -= PIXELS
    
    def move_body(self):
        if len(self.bodies) > 0:
            for i in range(len(self.bodies)-1,-1,-1):
                if i == 0:
                    self.bodies[0].posX = self.headX
                    self.bodies[0].posY = self.headY
                else:
                    self.bodies[i].posX = self.bodies[i-1].posX
                    self.bodies[i].posY = self.bodies[i-1].posY

    def add_body(self):
        body = Body((46,37,self.body_color + 10), self.headX, self.headY)
        self.bodies.append(body)
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.headX, self.headY, PIXELS, PIXELS))
        if len(self.bodies) > 0:
            for body in self.bodies:
                body.draw(surface)

    def die(self):
        self.headX = random.randrange(0, WIDTH, PIXELS)
        self.headY = random.randrange(0, HEIGHT, PIXELS)
        self.bodies = []
        self.body_color = 50
        self.state = "STOP"
class Collision:
    def bt_snake_and_apple(self, snake, apple):
        distance = math.sqrt(math.pow((snake.headX-apple.posX),2) + math.pow((snake.headY-apple.posY),2))
        return distance < PIXELS
    def bt_snake_and_walls(self,snake):
        if snake.headX < 0 or snake.headX > WIDTH - PIXELS or snake.headY < 0 or snake.headY > HEIGHT - PIXELS:
            return True
        return False
    def bt_head_and_body(self,snake):
        for body in snake.bodies:
            distance = math.sqrt(math.pow((snake.headX-body.posX),2) + math.pow((snake.headY-body.posY),2))
            if distance < PIXELS:
                return True
        return False
class Body:
    def __init__(self, color, posX, posY):
        self.color = color
        self.posX = posX
        self.posY = posY
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.posX, self.posY, PIXELS, PIXELS))
class Score:
    def __init__(self):
        self.points = 0
        self.font = pygame.font.SysFont('monospace', 30, bold = False)
        self.highscore = 0
    def increase(self):
        self.points += 100
    def reset(self):
        self.points = 0
    def show(self, surface):
        lbl = self.font.render("Score: " +str(self.points),1, BLACK)
        surface.blit(lbl,(5,5))
    def highscoreshow(self, surface):
        lbl = self.font.render("HighScore: " +str(self.highscore),1, BLACK)
        surface.blit(lbl,(320,5))
#Main fct:
def main():
   pygame.init()
   screen  = pygame.display.set_mode((WIDTH, HEIGHT))
   pygame.display.set_caption("Snake")

   #Objects
   background = Background()
   apple = Apple()
   snake = Snake()
   collision = Collision()
   score = Score()

   #MainLoop
   while True:
        background.draw(screen)
        snake.draw(screen)
        apple.draw(screen)
        score.show(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if snake.state != "DOWN":
                        snake.state = "UP"
                if event.key == pygame.K_DOWN:
                    if snake.state != "UP":
                        snake.state = "DOWN"
                if event.key == pygame.K_RIGHT:
                    if snake.state != "LEFT":
                        snake.state = "RIGHT"
                if event.key == pygame.K_LEFT:
                    if snake.state != "RIGHT":
                        snake.state = "LEFT"
                if event.key == pygame.K_SPACE:
                    snake.state = "STOP"

        if collision.bt_snake_and_apple(snake,apple):
            apple.spawn()
            snake.add_body()
            score.increase()
        #movement
        if snake.state != "STOP":
            snake.move_body()
            snake.move_head()
        if collision.bt_snake_and_walls(snake):
            snake.die()
            apple.spawn()
            score.reset()
            score.highscore = score.points
        if collision.bt_head_and_body(snake):
            snake.die()
            apple.spawn()
            score.reset()
        pygame.time.delay(100)
        pygame.display.update() #updates game screen.
main()