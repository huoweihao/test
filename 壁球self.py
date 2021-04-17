import sys,pygame

pygame.init()
size=width,height=600,400
BLACK=0,0,0
screen=pygame.display.set_mode(size,pygame.RESIZABLE)
pygame.display.set_caption("Pygame壁球","Python")
ball=pygame.image.load("ball.gif")
print(type(ball))
ballrect=ball.get_rect()
print(type(ballrect))
fps=150
fclock=pygame.time.Clock()

while True:
    for event in pygame.event.get():
        print(type(event))
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                while True:
                    screen.fill(BLACK)
                    ballrect=ballrect.move(-1,0)
                    screen.blit(ball,ballrect)
                    pygame.display.update()
                    fclock.tick(fps)
                    if pygame.event.poll().type==pygame.KEYUP:
                        break
            if event.key==pygame.K_RIGHT:
                while True:
                    screen.fill(BLACK)
                    ballrect=ballrect.move(1,0)
                    screen.blit(ball,ballrect)
                    pygame.display.update()
                    fclock.tick(fps)
                    if pygame.event.poll().type==pygame.KEYUP:
                        break
            if event.key==pygame.K_UP:
                while True:
                    screen.fill(BLACK)
                    ballrect=ballrect.move(0,-1)
                    screen.blit(ball,ballrect)
                    pygame.display.update()
                    fclock.tick(fps)
                    if pygame.event.poll().type==pygame.KEYUP:
                        break
            if event.key==pygame.K_DOWN:
                while True:
                    screen.fill(BLACK)
                    ballrect=ballrect.move(0,1)
                    screen.blit(ball,ballrect)
                    pygame.display.update()
                    fclock.tick(fps)
                    if pygame.event.poll().type==pygame.KEYUP:
                        break
        elif event.type==pygame.VIDEORESIZE:
            size=width,height=event.size[0],event.size[1]
            screen=pygame.display.set_mode(size,pygame.RESIZABLE)
            
    screen.fill(BLACK)
    screen.blit(ball,ballrect)
    pygame.display.update()
    fclock.tick(fps)
