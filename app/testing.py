import pygame
import threading
import time
import os

# print(os.getcwd())

pygame.mixer.init()

can_play = True

def play_sound(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def play_async(file):
    threading.Thread(target=play_sound, args=(file,)).start()

while True:

    access = "granted"   # or "denied"

    if access == "granted" and can_play:
        play_async("app/sounds/access_granted.mp3")
        can_play = False

    elif access == "denied" and can_play:
        play_async("app/sounds/access_granted.mp3")
        can_play = False

    if not can_play:
        time.sleep(4)
        can_play = True
