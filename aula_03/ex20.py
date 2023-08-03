# Faça um programa que rode um audio em mp3

import pygame
pygame.mixer.init()
pygame.mixer.music.load("exercises/Musica.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue 
