import pygame
from pygame.locals import *
from sys import exit
# init pygame and define the size of the screen
pygame.init()
SCREEN_SIZE = (800, 600)
# create a display surface
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
# set the format of the text
font = pygame.font.SysFont("arial", 16);
font_height = font.get_linesize()
event_text = []
while True:
    # get the event
    event = pygame.event.wait()
    # add the event_text
    event_text.append(str(event))
    # get the current event text
    event_text = event_text[int(-SCREEN_SIZE[1]/font_height):]
    if event.type == QUIT:
        exit()
    # set the background color
    screen.fill((255, 255, 255))
    # get the display position
    y = SCREEN_SIZE[1]-font_height
    for text in reversed(event_text):
        # blit the text to the screen
        screen.blit( font.render(text, True, (0, 0, 0)), (0, y) )
        y-=font_height
    # display the text on the screen that have been created in the memory
    pygame.display.update()
