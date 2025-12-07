#Faça um programa em python que abra e reproduza audio de um arquivo mp3
import pygame
#iniciar o pygame
pygame.init()
pygame.mixer.music.load('Ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()



