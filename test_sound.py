import pygame
pygame.mixer.init()
pygame.mixer.music.load("sound/alarm.wav")
pygame.mixer.music.play()

input("Press Enter to exit")