import random
import pygame

from constants import UP, DOWN, RIGHT, LEFT, GRID_SIZE, WIN_WIDTH, WIN_HEIGHT, SNAKE_COLOR, SNAKE_STROKE_COLOR
from grid import get_center_position
from utils import draw_rect

class Snake:
  def __init__(self):
    # Масив пар координат. Кожна пара представляє одину частину тіла змії
    self.body = [get_center_position()]
    self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
    self.color = SNAKE_COLOR

  def get_head_position(self):
    return self.body[0]

  def turn(self, direction):
    # Якщо довжина змії більше 1, то вона не може змінити свій напрямок
    # на протилежний. Можливими є лише 3 напрямки відносно голови:
    # 1. Продовжувати рух в тому самому напрямку,
    # 2. Повернути праворуч відносно голови
    # 3. Повернути ліворуч відносно голови
    if len(self.body) > 1 and self.is_reverse_direction(direction):
      return
    else:
      self.direction = direction

  def is_reverse_direction(self, direction):
    return (direction[0] * -1, direction[1] * -1) == self.direction

  def increase_length(self):
    # Отримуємо позицію останнього сегмента
    (x, y) = self.body[-1]
    self.body.append((x, y))

  def move(self):
    current_position = self.get_head_position()
    new_position = (
      (current_position[0] + self.direction[0] * GRID_SIZE) % WIN_WIDTH,
      (current_position[1] + self.direction[1] * GRID_SIZE) % WIN_HEIGHT
    )

    # Перевіряємо чи вдарилася змія об себе
    if (len(self.body) > 2 and new_position in self.body):
      self.reset()
    else:
      self.body.insert(0, new_position)
      self.body.pop()

  def reset(self):
    self.body = [get_center_position()]
    self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

  def draw(self, surface):
    for (x, y) in self.body:
      draw_rect(surface, x, y, fill=SNAKE_COLOR, stroke=SNAKE_STROKE_COLOR)

  def handle_keys(self, event):
    if event.key == pygame.K_UP:
      self.turn(UP)
    elif event.key == pygame.K_DOWN:
      self.turn(DOWN)
    elif event.key == pygame.K_LEFT:
      self.turn(LEFT)
    if event.key == pygame.K_RIGHT:
      self.turn(RIGHT)
