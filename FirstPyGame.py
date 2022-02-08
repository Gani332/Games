import pygame

pygame.init()

win = pygame.display.set_mode((1000, 500))
Title = pygame.display.set_caption("Don't Get Moored")
BLACK = (0, 0, 0)

x = 900
y = 440
width = 50
height = 50
vel = 5

isJump = False
jumpCount = 10

isJump2 = False
jumpCount2 = 10

px = 50
py = 440
pwidth = 50
pheight = 50
pvel = 5

x2 = 10
y2 = 10
width2 = 10
height2 = 500

x3 = 980
y3 = 10
width3 = 10
height3 = 500

##text = win.blit("")


# MainLoop
run = True
while run:
    ##win.blit(text)
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 1000 - width - vel:
        x += vel
    if not isJump:
        if keys[pygame.K_UP]:
            isJump = True

    else:
        if jumpCount >= -10:
            neg1 = 1
            if jumpCount < 0:
                neg1 = -1
            y -= (jumpCount ** 2) * 0.5 * neg1
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    if keys[pygame.K_a] and px > pvel:
        px -= pvel
    if keys[pygame.K_d] and px < 1000 - pwidth - pvel:
        px += pvel

    if not (isJump2):
        if keys[pygame.K_w]:
            isJump2 = True
    else:
        if jumpCount2 >= -10:
            neg = 1
            if jumpCount2 < 0:
                neg = -1
            py -= (jumpCount2 ** 2) * 0.5 * neg
            jumpCount2 -= 1
        else:
            isJump2 = False
            jumpCount2 = 10

    win.fill((0, 0, 0))
    pygame.draw.rect(win, [0, 255, 0], (x, y, width, height))
    pygame.draw.rect(win, (255, 0, 0), (px, py, pwidth, pheight))

    pygame.display.update()

pygame.quit()
