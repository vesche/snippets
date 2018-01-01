#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# pygame raycaster
#

import math
import pygame
from pygame.locals import *

m = [ [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
      [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
      [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
      [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
      [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
      [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
      [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
      [1,2,1,2,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
      [1,0,0,0,0,2,0,0,0,3,0,0,0,0,0,0,0,0,0,1],
      [1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1],
      [1,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1],
      [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
      [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
      [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
      [1,0,0,0,1,0,2,0,3,0,2,0,1,0,0,0,0,0,0,1],
      [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
      [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
      [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
      [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] ]

# constants
WIDTH = 1000
HEIGHT = 800
MOVSPEED = 0.03
ROTSPEED = 0.02

# trig constants
TGM = (math.cos(ROTSPEED), math.sin(ROTSPEED))
ITGM = (math.cos(-ROTSPEED), math.sin(-ROTSPEED))
COS, SIN = 0, 1

# init vars
positionX = 3.0
positionY = 7.0
directionX = 1.0
directionY = 0.0
planeX = 0.0
planeY = 0.5

# init pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("raycaster")
keys = [False]*500 # turn this into dict later

while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            keys[event.key] = True
        elif event.type == KEYUP:
            keys[event.key] = False

    if keys[K_ESCAPE]:
        pygame.display.quit()
        pygame.quit()

    if keys[K_LEFT]:
        oldDirectionX = directionX
        directionX = directionX * ITGM[COS] - directionY * ITGM[SIN]
        directionY = oldDirectionX * ITGM[SIN] + directionY * ITGM[COS]
        oldPlaneX = planeX
        planeX = planeX * ITGM[COS] - planeY * ITGM[SIN]
        planeY = oldPlaneX * ITGM[SIN] + planeY * ITGM[COS]

    if keys[K_RIGHT]:
        oldDirectionX = directionX
        directionX = directionX * TGM[COS] - directionY * TGM[SIN]
        directionY = oldDirectionX * TGM[SIN] + directionY * TGM[COS]
        oldPlaneX = planeX
        planeX = planeX * TGM[COS] - planeY * TGM[SIN]
        planeY = oldPlaneX * TGM[SIN] + planeY * TGM[COS]

    if keys[K_UP]:
        if not m[int(positionX + directionX * MOVSPEED)][int(positionY)]:
            positionX += directionX * MOVSPEED
        if not m[int(positionX)][int(positionY + directionY * MOVSPEED)]:
            positionY += directionY * MOVSPEED

    if keys[K_DOWN]:
        if not m[int(positionX - directionX * MOVSPEED)][int(positionY)]:
            positionX -= directionX * MOVSPEED
        if not m[int(positionX)][int(positionY - directionY * MOVSPEED)]:
            positionY -= directionY * MOVSPEED

    # clear screen
    screen.fill((25,25,25))
    pygame.draw.rect(screen, (50,50,50), (0, HEIGHT/2, WIDTH, HEIGHT/2))

    for x in range(WIDTH):
        mapX = int(positionX)
        mapY = int(positionY)

        cameraX = 2.0 * x / WIDTH - 1.0
        rayDirX = directionX + planeX * cameraX
        rayDirY = directionY + planeY * cameraX + .0000001
        deltaDistX = math.sqrt(1.0 + (rayDirY * rayDirY) / (rayDirX * rayDirX))
        deltaDistY = math.sqrt(1.0 + (rayDirX * rayDirX) / (rayDirY * rayDirY))

        if rayDirX < 0:
            stepX = -1
            sideDistX = (positionX - mapX) * deltaDistX
        else:
            stepX = 1
            sideDistX = (mapX + 1.0 - positionX) * deltaDistX
        if rayDirY < 0:
            stepY = -1
            sideDistY = (positionY - mapY) * deltaDistY
        else:
            stepY = 1
            sideDistY = (mapY + 1.0 - positionY) * deltaDistY

        hit = False
        while not hit:
            if sideDistX < sideDistY:
                sideDistX += deltaDistX
                mapX += stepX
                side = False
            else:
                sideDistY += deltaDistY
                mapY += stepY
                side = True
            if m[mapX][mapY] > 0:
                hit = True

        if not side:
            perpWallDist = abs((mapX - positionX + (1.0 - stepX) / 2.0) / rayDirX)
        else:
            perpWallDist = abs((mapY - positionY + (1.0 - stepY) / 2.0) / rayDirY)

        lineHeight = abs(int(HEIGHT / (perpWallDist + .0000001)))

        drawStart = -lineHeight / 2.0 + HEIGHT / 2.0
        drawEnd = lineHeight / 2.0 + HEIGHT / 2.0
        if drawStart < 0:
            drawStart = 0
        if drawEnd >= HEIGHT:
            drawEnd = HEIGHT - 1

        # colors
        wallcolors = [[], [150,0,0], [0,150,0], [0,0,150]]
        color = wallcolors[m[mapX][mapY]]
        if side:
            for k, v in enumerate(color):
                color[k] = int(v / 1.2)

        pygame.draw.line(screen, color, (x, drawStart), (x, drawEnd), 1)

    # draw anything else here

    # update screen
    pygame.event.pump()
    pygame.display.flip()
