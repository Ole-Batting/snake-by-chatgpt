import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (400, 400)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Snake")

# Set the dimensions of the snake
snake_size = 10

# Set the initial position of the snake
snake_position = [100, 100]

# Set the initial movement direction of the snake
snake_direction = "right"

# Set the initial snake body, which is just a list of coordinates
snake_body = [[100, 100], [90, 100], [80, 100], [70, 100]]

# Set the initial position of the food
food_position = [random.randrange(1, (window_size[0] // snake_size)) * snake_size,
                 random.randrange(1, (window_size[1] // snake_size)) * snake_size]
food_spawn = True

# Set the initial score to 0
score = 0

# Set the initial game speed
speed = 10

# Set the font for the score text
font = pygame.font.SysFont("times new roman", 35)

# Set the game over flag to False
game_over = False

# Run the game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if snake_direction == "up":
                    snake_direction = "left"
                elif snake_direction == "down":
                    snake_direction = "right"
                elif snake_direction == "left":
                    snake_direction = "down"
                elif snake_direction == "right":
                    snake_direction = "up"
            if event.key == pygame.K_RIGHT:
                if snake_direction == "up":
                    snake_direction = "right"
                elif snake_direction == "down":
                    snake_direction = "left"
                elif snake_direction == "left":
                    snake_direction = "up"
                elif snake_direction == "right":
                    snake_direction = "down"

    # Update the snake position
    if snake_direction == "up":
        snake_position[1] -= snake_size
    if snake_direction == "down":
        snake_position[1] += snake_size
    if snake_direction == "left":
        snake_position[0] -= snake_size
    if snake_direction == "right":
        snake_position[0] += snake_size

    # Update the snake body
    snake_body.insert(0, list(snake_position))

    # Check if the snake has collided with the walls
    if snake_position[0] < 0 or snake_position[0] > window_size[0] - snake_size:
        game_over = True
    if snake_position[1] < 0 or snake_position[1] > window_size[1] - snake_size:
        game_over = True

    # Check if the snake has collided with its own body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over = True
    
    # Check if the snake has eaten the food
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 1
        food_spawn = False

    # Spawn a new piece of food if the snake has eaten the current one
    if not food_spawn:
        food_position = [random.randrange(1, (window_size[0] // snake_size)) * snake_size,
                        random.randrange(1, (window_size[1] // snake_size)) * snake_size]
    food_spawn = True

    # Remove the last block of the snake's body if the snake hasn't eaten any food
    if len(snake_body) > score + 1:
        snake_body.pop()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the snake
    for pos in snake_body:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(pos[0], pos[1], snake_size, snake_size))

    # Draw the food
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(food_position[0], food_position[1], snake_size, snake_size))

    # Draw the score text
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.update()

    # Set the frame rate of the game
    pygame.time.Clock().tick(speed)

# Quit Pygame
pygame.quit()

