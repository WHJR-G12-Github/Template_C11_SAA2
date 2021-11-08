import pygame
pygame.init()
screen=pygame.display.set_mode((400,600))
pygame.display.set_caption('Infinite Flying Bird Game')
images={}
images["bg"] = pygame.image.load("bg1.png").convert_alpha()
images["ground"] = pygame.image.load("base.png").convert_alpha()
images["bird"] = pygame.image.load("bird.png").convert_alpha()
images["pipe"] = pygame.image.load("pipe.png").convert_alpha()
groundx=0
speed=0
class Bird:
    bird=pygame.Rect(100,250,30,30)
    
    def movedown(self):
        global speed
        gravity=0.2
        speed=speed+gravity
        self.bird.y=self.bird.y+speed
    def moveup(self):
        global speed
        # Decrement the value of 'speed' to make the bird move up faster
        
    def display(self):
        screen.blit(images["bird"],self.bird)

class Pipe:
    bpipe=pygame.Rect(250,400,40,320)
    def display(self):
      screen.blit(images["pipe"],self.bpipe)
      
bird1=Bird()
pipe1=Pipe()
while True:  
  screen.blit(images["bg"],[0,0])
  groundx-=5
  if groundx<-450:
      groundx=0
  screen.blit(images["ground"],[groundx,550])
  bird1.movedown()
  bird1.display()
  pipe1.display()
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
        pygame.quit()
  
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_SPACE:
            bird1.moveup()  
  
  pygame.display.update()
  
  pygame.time.Clock().tick(30)
