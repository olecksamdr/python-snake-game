import sys, random
import pygame

from constants import WIN_WIDTH, WIN_HEIGHT, GRID_SIZE, GRID_WIDTH, GRID_HEIGHT
from grid import draw_grid
from Snake import Snake
from Food import Food

def main():
  pygame.init()

  # Створюємо вікно нашої гри
  # TODO: що означають числа?
  win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), 0, 32)

  # Встановлюємо заголовок вікна
  pygame.display.set_caption('змійка')

  # Контролює FPS (кількість кадрів в секунду)
  # Точніше скільки разів в секунду наш ігровий цикл має виконуватися
  clock = pygame.time.Clock()

  # TODO: add comment
  surface = pygame.Surface(win.get_size())
  # TODO: add comment
  surface = surface.convert()

  snake = Snake()
  food = Food()

  # ігровий цикл
  # Якщо в нас не буде вічного циклу то програма просто завершить роботу
  while True:
    # Перевіряємо наявність подій в pygame.event.get()
    # Який повертає нам події, що відбулися. Такі як клім мишкою, натиснення клавіші,
    # закриття вікна на хрестик
    for event in pygame.event.get():
      # Тут перевіряємо чи користувач натиснув на хрестик, щоб закрити вікно
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        snake.handle_keys(event)

    draw_grid(surface)
    food.draw(surface)
    snake.draw(surface)
    snake.move()

    if snake.get_head_position() == food.position:
      snake.increase_length()
      food.change_position()

    # TODO: add comment
    win.blit(surface, (0, 0))
    pygame.display.update()

    # Використовуємо clock.tick щоб встановити кількість кадрів в секунду
    # Це означає, що наш цикл виконуватиметься 30 разів в секунду
    clock.tick(8)


main()