import pygame
import time

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bday Card")

b = pygame.image.load("images/balloon.jpg")
rs = pygame.transform.scale(b,(600,600))

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
    screen.blit(rs, (0,0))
    font = pygame.font.SysFont("SANS serif", 40)
    text = font.render("Happy Birthday!!!!", True, "black")
    screen.blit(text, (180,300))
    pygame.display.update()
    time.sleep(2)

    c= pygame.image.load("images/cake.jpg")
    rs1= pygame.transform.scale(c,(600,600))
    screen.blit(rs1, (0,0))
    text1 = font.render("Here is your cake!", True, "black")
    screen.blit(text1,(180,30))
    pygame.display.update()
    time.sleep(2)                           