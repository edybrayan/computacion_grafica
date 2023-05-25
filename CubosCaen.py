import pygame
import random
import time

pygame.init()

width = 800
height = 600

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cubos cayendo")

cubo_tam = 50
vel_caida = 2 

cubos = []

for _ in range(50):
    cubo_x = random.randint(0, width - cubo_tam)
    cubo_y = random.randint(-height, 0)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    cubo = [cubo_x, cubo_y, color]
    cubos.append(cubo)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for cubo in cubos:
        cubo[1] += vel_caida

        if cubo[1] >= height - cubo_tam:
            cubo[1] = height - cubo_tam

    window.fill((0, 0, 0))

    for cubo in cubos:
        color = cubo[2]
        pygame.draw.rect(window, color, (cubo[0], cubo[1], cubo_tam, cubo_tam))

    pygame.display.update()

    time.sleep(0.02)

pygame.quit()
