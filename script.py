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

# Beate when the program starts
actiive_length = 0
active_beat = 0

# Screen setup, visible title, and font
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Beat Maker')
label_font = pygame.font.Font('helvetica.ttf', 28)

# Frame speed and timer
FPS = 60
timer = pygame.time.Clock()

# While loop for when the program is running
run = True
while run:
    timer.tick(FPS)
    screen.fill(black)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

