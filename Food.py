import random
import pygame

from constants import GRID_SIZE, FOOD_COLOR, FOOD_STROKE_COLOR
from grid import get_random_position
from utils import draw_rect

class Food:
  def __init__(self):
    self.position = get_random_position()
    self.color = FOOD_COLOR

  def change_position(self):
    self.position = get_random_position()

  def draw(self, surface):
    (x, y) = self.position
    draw_rect(surface, x, y, fill=self.color, stroke=FOOD_STROKE_COLOR)
