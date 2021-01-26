import pygame

from constants import GRID_SIZE

def draw_rect(surface, x, y, fill, stroke):
  rect = pygame.Rect((x, y), (GRID_SIZE, GRID_SIZE))
  pygame.draw.rect(surface, fill, rect)
  pygame.draw.rect(surface, stroke, rect, 1)
