import pygame
import time

pygame.init()
pygame.mixer.music.load('../audio.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
     time.sleep(0.1)