import pygame
import sys
import random
import pickle
import os 


HIGH_SCORE_FILE = "highscore.dat"

def resource_path(filename):
    """Get the absolute path to a resource, works for PyInstaller."""
    if getattr(sys, "frozen", False):
        # Running in PyInstaller bundle
        return os.path.join(sys._MEIPASS, filename)
    return os.path.abspath(filename)

pygame.init()
pygame.mixer.init()



eat_sound = pygame.mixer.Sound(resource_path("eat.mp3"))
eat_sound.set_volume(0.5)

crash_sound = pygame.mixer.Sound(resource_path("crash.mp3"))
crash_sound.set_volume(0.5)

gameover_sound = pygame.mixer.Sound(resource_path("gameover.mp3"))
gameover_sound.set_volume(0.5)


pygame.mixer.music.load(resource_path("snaketheme.mp3"))
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)


WIDTH, HEIGHT = 640, 480
CELL = 20
BASE_FPS = 10

BLACK = (0, 0, 0)
DARK_GREEN = (0, 150, 0)
LIME_GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SnakeGame")
clock = pygame.time.Clock()
font = pygame.font.SysFont("ubuntu", 36)

def draw_block(color, pos):
    x, y = pos
    rect = pygame.Rect(x * CELL, y * CELL, CELL, CELL)
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, BLACK, rect, 2)  # segment lines

def draw_grid():
    for x in range(0, WIDTH, CELL):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, HEIGHT))
    for y in range(0, WIDTH, CELL):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (WIDTH, y)) 

def draw_walls():
    wall_thickness = 4
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, wall_thickness))
    pygame.draw.rect(screen, WHITE, (0, HEIGHT - wall_thickness, WIDTH, wall_thickness))
    pygame.draw.rect(screen, WHITE, (0, 0, wall_thickness, HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH- wall_thickness, 0, wall_thickness, HEIGHT))           

def load_high_score():
    try:
        with open(HIGH_SCORE_FILE, "rb") as f:
            return pickle.load(f)
    except:
        return 0     

def save_high_score(score, high_score):
    if score > high_score:
        high_score = score
        with open(HIGH_SCORE_FILE, "wb") as f:
            pickle.dump(high_score, f)
    return high_score

def random_pos(snake):
    while True:
        pos = (random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))
        if pos not in snake:
            return pos

def game_over_screen(score):
    screen.fill(BLACK)
    game_over_text = font.render("Game Over", True, WHITE)
    score_text = font.render(f"Score: {score}", True, WHITE)
    restart_text = font.render("Press R to restart or Q to quit", True, WHITE)
    pygame.mixer.music.stop()
    screen.blit(game_over_text, [WIDTH//2 - 80, HEIGHT//2 - 60])
    screen.blit(score_text, [WIDTH//2 - 50, HEIGHT//2 - 20])
    screen.blit(restart_text, [WIDTH//2 - 170, HEIGHT//2 + 20])
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                 pygame.mixer.music.play(-1)
                 return
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

def run_game():
    # Start snake fully inside the grid
    snake = [(5, 5), (6, 5), (7, 5)]
    direction = (1, 0)
    food = random_pos(snake)
    score = 0
    high_score = load_high_score()
    high_score = save_high_score(score, high_score)

     

    while True:
        # Handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)

        # Move snake
        head_x, head_y = snake[-1]
        new_head = (head_x + direction[0], head_y + direction[1])

        # Collision check BEFORE appending the head
        if (new_head[0] < 0 or new_head[0] >= WIDTH // CELL or
            new_head[1] < 0 or new_head[1] >= HEIGHT // CELL or
            new_head in snake):
             crash_sound.play()
             gameover_sound.play()
             game_over_screen(score)
             high_score = save_high_score(score, high_score)
             game_over_screen(score)
             return

        # Append new head
        snake.append(new_head)

        # Check if food eaten
        if new_head == food:
            score += 10
            eat_sound.play()
            food = random_pos(snake)
        else:
            snake.pop(0)  # remove tail

        # Draw everything
        screen.fill(BLACK)
        draw_grid()
        
           # Draw score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, [10, 10])
        score_text = font.render(f"Score: {score}  High: {high_score}", True, WHITE)
        screen.blit(score_text, [10, 10])


        # Draw snake using original method
        for i in range(len(snake)):
            if i == len(snake) - 1:
                draw_block(LIME_GREEN, snake[i])  # head
            else:
                draw_block(DARK_GREEN, snake[i])  # body

        # Draw food
        draw_block(RED, food)

        draw_walls()

        pygame.display.update()
 
        if score >= 50:
         current_fps = BASE_FPS + (score - 50) // 50
        else:
         current_fps = BASE_FPS 

        clock.tick(current_fps)     
        

if __name__ == "__main__":
    while True:
        run_game()

