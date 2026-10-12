import pygame
from time import sleep
import random

images = ("horrorpicture,jpg", "picture", "picture2")
sounds = ("485802__grez1__scream14.mp3", "sound", "sound2")

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("485802__grez1__scream14.mp3")
image = pygame.image.load("horrorpicture.jpg")

while True:
    sleep(random.randint(30, 300))
    window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    window.blit(image, (5,5))
    pygame.display.update()
    pygame.mixer.music.play()
    sleep(3)
    pygame.display.quit()
