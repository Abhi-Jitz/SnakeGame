import pygame
import random

pygame.init()# init game

# color
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

# screen
screen_width = 900
screen_height = 600

# setting display
game_window = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)

def text_screen(text, color ,x ,y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x,y])

def plot_snake(game_window, color, snk_list, snk_size):
    for x,y in snk_list:
        pygame.draw.rect(game_window,color, [x,y,snk_size,snk_size])

def game_loop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    food_x = random.randint(20, screen_width-20)
    food_y = random.randint(60, screen_height -20)
    score = 0
    init_velocity = 4
    snake_size = 25
    food_size = 10
    fps = 60   # fps 
    while not exit_game:
        if game_over:
            game_window.fill(white)
            text_screen("Game Over! Press Enter To Continue", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                score +=1
                food_x = random.randint(20, screen_width - 30)
                food_y = random.randint(60, screen_height - 30)
                snk_length +=5

            game_window.fill(white)
            text_screen("Score: " + str(score * 10), red, 5, 5)
            # Food size and position
            pygame.draw.rect(game_window, red, [food_x, food_y, food_size, food_size])
            pygame.draw.line(game_window, red, (0,40), (900,40),5)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            # game over in head touching snake
            if head in snk_list[:-1]:
                game_over = True
            
            # game over in head touchiing border
            if snake_x<0 or snake_x>screen_width-20 or snake_y<50 or snake_y>screen_height-20:
                game_over = True
            plot_snake(game_window, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
game_loop()