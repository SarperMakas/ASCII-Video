
import cv2
import pygame
import math

cap = cv2.VideoCapture(0)

pygame.init()
fontSize = 3
ret, frame = cap.read()
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

h = int(len(frame)/3)
w = int(len(frame[0])/3)

frame = cv2.resize(frame, (w, h))

pygame.init()
screen = pygame.display.set_mode((fontSize * len(frame[0]), fontSize * len(frame)))
pygame.display.set_caption("Video to text")

run = True

font = pygame.font.Font('CourierPrime-Regular.ttf', 5)
density = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
length = len(density)

while run:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (w, h))

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    # draw
    screen.fill((0, 0, 0))  # background black
    t = ""
    for i in range(len(frame)): # row
        for j in range(len(frame[0])): # col
            OldRange = (255 - 0)
            NewRange = (0 - length)
            avg = (int(frame[i][j][0])+int(frame[i][j][1])+int(frame[i][j][2]))/3
            index = math.floor((((avg - 0) * NewRange) / OldRange) + 0)
            if index == length:
                index -= 1
            t += density[index]
        text = font.render(t, True, (255, 255, 255), (0, 0, 0))
        rect = text.get_rect(topleft=(0, i*fontSize))
        screen.blit(text, rect)
        t = ""

    pygame.display.flip()

pygame.display.quit()
