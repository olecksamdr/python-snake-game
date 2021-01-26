import pygame
import random

from constants import GRID_SIZE, GRID_WIDTH, GRID_HEIGHT, GRID_FIRST_COLOR, GRID_SECOND_CLOR

def get_center_position():
  return (
    GRID_WIDTH // 2 * GRID_SIZE,
    GRID_HEIGHT // 2 * GRID_SIZE,
  )

def get_random_position():
  x = random.randint(0, GRID_WIDTH - 1) * GRID_SIZE
  y = random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE

  return (x, y)

def draw_grid(surface):
  for y in range(0, int(GRID_HEIGHT)):
    for x in range(0, int(GRID_WIDTH)):
      rect = pygame.Rect(
        (x * GRID_SIZE, y * GRID_SIZE),
        (GRID_SIZE, GRID_SIZE),
      )

      pygame.draw.rect(
        surface,
        GRID_FIRST_COLOR if (x + y) % 2 == 0 else GRID_SECOND_CLOR,
        rect,
      )