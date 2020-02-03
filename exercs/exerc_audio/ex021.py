'''Faca um programa em python que abra e reproduza um audio de arquivo mp3'''

import pygame
pygame.mixer.init()
pygame.mixer.music.load('its-me-mario.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()







