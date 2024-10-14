# Snake Game with Adarsh Singh

Welcome to the Snake Game project created using Python and Pygame! This game allows users to control a snake that grows when it eats food while avoiding collisions with itself and the walls.

## Features

- **Simple Gameplay**: Navigate the snake using arrow keys.
- **Score Tracking**: The score increases each time the snake eats food.
- **Player Information Collection**: Collects player's name, phone number, and age (in the background).
- **System Information Display**: Displays system and CPU information after game setup.

## Installation Instructions

Follow these instructions to install and run the game on different operating systems, including Termux.

### For Linux (Debian/Ubuntu-based)

1. Open your terminal.
2. Update your package list:
   ```bash
   sudo apt update
Install Python and pip:
bash

sudo apt install python3 python3-pip
Clone the repository:
bash

git clone https://github.com/adarshsingh10100/games.git
Navigate to the project directory:
bash

cd games
Install the required Python modules:
bash

pip install pygame requests psutil
Run the game:
bash

python3 mobile.py
For macOS
Open your terminal.
Install Homebrew if you haven't already:
bash

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
Install Python:
bash

brew install python
Clone the repository:
bash

git clone https://github.com/adarshsingh10100/games.git
Navigate to the project directory:
bash

cd games
Install the required Python modules:
bash

pip3 install pygame requests psutil
Run the game:
bash

python3 mobile.py
For Windows
Download and install Python from python.org. Make sure to check the box to add Python to your PATH.
Open Command Prompt.
Clone the repository:
bash

git clone https://github.com/adarshsingh10100/games.git
Navigate to the project directory:
bash

cd games
Install the required Python modules:
bash

pip install pygame requests psutil
Run the game:
bash

python mobile.py
For Termux (Android)
Open Termux.
Update the package list:
bash

pkg update
Install Python:
bash

pkg install python
Install pip:
bash

pkg install python-pip
Install required modules:
bash

pip install pygame requests psutil
Clone the repository:
bash

git clone https://github.com/adarshsingh10100/games.git
Navigate to the project directory:
bash

cd games
Run the game:
bash

python mobile.py
Usage
Use the arrow keys to control the direction of the snake.
The snake will grow each time it eats food (red squares).
Avoid running into the walls or the snake's own body.
Note
The game collects player data (name, phone number, and age) in the background for game personalization and experience enhancement purposes. System and CPU information are also displayed after running the game.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Special thanks to Pygame for the game development library.
Inspired by classic Snake games.
