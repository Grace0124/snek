import pygame
import time
import random

snake_speed = 30

# window size
window_x = 720
window_y = 480

# colors and font
dark = (52, 78, 65)
light = (163, 177, 138)
medium = (218, 215, 205)

pygame.init()
pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

# default snake position and direction
snake_position = [100, 50]
snake_body = [[100, 50],[90, 50], [80, 50], [70, 50]]
direction = "RIGHT"
change_to = direction

# places fruit randomly in [10, 720]
fruit_position = [random.randrange(1, (window_x//10))*10,
             random.randrange(1, (window_y//10))*10]
fruit_spawn = True
fruit2_position = [random.randrange(1, (window_x//10))*10,
             random.randrange(1, (window_y//10))*10]
fruit2_spawn = True
# score
score = 0
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont('georgia', 15)
    score_surface = score_font.render(f'Score: {score}', True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

def game_over():
    game_over_font = pygame.font.SysFont('georgia', 50)
    game_over_surface = game_over_font.render(f'Your Score is: {score}', True, medium)
    game_over_rect = game_over_surface.get_rect()

    game_over_rect.midtop = (window_x /2, window_y /4) # set text to middle of screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip() # update entire display

    time.sleep(2) # quit after 2 seconds

    pygame.quit()
    quit()


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = "UP"
            elif event.key == pygame.K_DOWN:
                direction = "DOWN"
            elif event.key == pygame.K_LEFT:
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT:
                direction = "RIGHT"
        
    if direction == "UP":
        snake_position[1] -= 10
    elif direction == "DOWN":
        snake_position[1] += 10
    elif direction == "LEFT":
        snake_position[0] -= 10
    elif direction == "RIGHT":
        snake_position[0] += 10
    

    # increase size of snake body
    snake_body.insert(0, list(snake_position))
    # update score
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    elif snake_position[0] == fruit2_position[0] and snake_position[1] == fruit2_position[1]:
        score += 10
        fruit2_spawn = False
    else: # decrease size if we did not touch a fruit
        snake_body.pop()
    
    # respawn fruit
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                          random.randrange(1, (window_y//10)) * 10]
        fruit_spawn = True
    
    if not fruit2_spawn:
        fruit2_position = [random.randrange(1, (window_x//10)) * 10, 
                          random.randrange(1, (window_y//10)) * 10]
        fruit2_spawn = True
    
    game_window.fill(dark)

    # draw the snake
    for pos in snake_body:
        pygame.draw.rect(game_window, light, pygame.Rect(pos[0], pos[1], 10, 10))
    
    # draw fruit
    pygame.draw.rect(game_window, light, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))
    pygame.draw.rect(game_window, light, pygame.Rect(fruit2_position[0], fruit2_position[1], 10, 10))

    # checking if game is over
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    show_score(1, light, 'georgia', 20)

    pygame.display.update()
    
    fps.tick(snake_speed)

    
