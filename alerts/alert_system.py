import pygame
import os

pygame.mixer.init()

# Absolute path (fixes most sound errors)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sound_path = os.path.join(BASE_DIR, "sound", "alarm.wav")

def play_alarm():
    try:
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play()
    except Exception as e:
        print("Alarm sound error:", e)