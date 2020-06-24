import pygame, sys, os
from random import uniform

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

display_size = (720,480)

screen = pygame.display.set_mode(display_size)
pygame.display.set_caption("Particles")
FPS = pygame.time.Clock()

font = pygame.font.SysFont("Arial",20)

class Partcle(pygame.sprite.Sprite):
    def __init__(self,x,y,hsp,vsp,grav):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.vsp = vsp
        self.hsp = hsp
        self.grav = grav

        self.images = [pygame.image.load("img/part1.png"),
                       pygame.image.load("img/part2.png"),
                       pygame.image.load("img/part3.png"),
                       pygame.image.load("img/part4.png"),
                       pygame.image.load("img/part5.png"),
                       pygame.image.load("img/part6.png"),
                       pygame.image.load("img/part7.png")]

        self.curImg = 0
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.range1 = round(uniform(-self.vsp,self.vsp),2)
        self.range2 = round(uniform(-self.hsp,self.hsp),2)

    def update(self):
        self.rect[0] = self.x
        self.rect[1] = self.y

        self.curImg += 0.1
        self.image = self.images[int(self.curImg)]

        self.range1 += self.grav
        self.x += self.range2
        self.y += self.range1

        if round(self.curImg) > 6 or self.y > display_size[1] or self.y < 0 or self.x > display_size[0] or self.x < 0:
            partGroup.remove(self)


def add(var,ad,lim):
    var += ad
        
    if lim > 0 and var >= lim or lim <= 0 and var <= lim:
        var = lim

    return var

partGroup = pygame.sprite.Group()

vsp = 5
grav = 0.3
hsp = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                vsp = add(vsp, 1, 20)
            elif event.button == 5:
                vsp = add(vsp, -1, 0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                grav = add(grav,0.1,2)
            elif event.key == pygame.K_s:
                grav = add(grav, -0.1, -2)
            if event.key == pygame.K_d:
                hsp = add(hsp, 1, 20)
            elif event.key == pygame.K_a:
                hsp = add(hsp, -1, 0)

    x, y = pygame.mouse.get_pos()
    press = pygame.mouse.get_pressed()

    if press[0]:
        for i in range(8):
            part = Partcle(x, y, hsp, vsp, grav)
            partGroup.add(part)

    screen.fill((0,0,0))
    partGroup.update()
    partGroup.draw(screen)

    text = font.render("Hold the left button to generate particles",False,(255,255,255))
    spriteCount = font.render("Particle Count: " + str(len(partGroup)), False, (255, 255, 255))
    fpsCount = font.render("FPS: " + str(round(FPS.get_fps())), False, (255, 255, 255))
    inf = font.render("Vsp Range (Mouse Wheel): " + str(vsp) + " | Hsp Range (A/D): " + str(hsp) + " | Gravity (W/S): " + str(round(grav,2)),False,(255,255,255))

    screen.blit(text, [5, 0])
    screen.blit(spriteCount, [5, 450])
    screen.blit(fpsCount, [655, 450])
    screen.blit(inf, [5, 30])

    pygame.display.update()
    FPS.tick(60)