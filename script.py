# Imports
import pygame
from pygame import mixer
pygame.init()

# Height and width
WIDTH = 1500
HEIGHT = 800

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

# Screen setup, visible title, and font
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Beat Maker')
label_font = pygame.font.Font('helvetica.ttf', 28)

# Frame speed and timer
FPS = 60
timer = pygame.time.Clock()