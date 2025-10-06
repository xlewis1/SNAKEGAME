🐍 Classic Snake Game (Python + Pygame)
A faithful Snake remake written in Python using Pygame.
This project recreates the classic Nokia Snake game with modern Python and Pygame, including smooth movement, sounds, high score saving, and increasing speed as you progress.
🎮 Features
Classic Snake gameplay — start with a small snake and grow as you eat.
Dynamic speed increase every 50 points.
Dark green body with lime head for classic style.
Black segment lines for visible body segments.
Sound effects: eating, crash, game over.
Background music with looping support.
High score saving between sessions.
Clean code, easy to read and modify for learning purposes.
🧰 Requirements
Python 3
Pygame
📝 Installation
1️⃣ Python & Pip
Make sure Python 3 is installed:
python3 --version
Ensure pip is installed:
python3 -m ensurepip --default-pip
2️⃣ Install Pygame
pip install pygame
On Windows, if pip isn’t recognized:
py -m pip install pygame
🚀 How to Play
macOS Users
Download the ZIP: SnakeGame_Mac.zip.
Unzip it and open SnakeGame to play.
Everything you need (sounds, music) is included.
Windows/Linux Users
Download all files:
SnakeGame.py
snaketheme.mp3
eat.mp3
crash.mp3
gameover.mp3
Keep all files in the same folder.
Run the game:
python SnakeGame.py
Optional: Build your own executable using PyInstaller:
pyinstaller --onefile --add-data "snaketheme.mp3:." --add-data "eat.mp3:." --add-data "crash.mp3:." --add-data "gameover.mp3:." SnakeGame.py
🎹 Controls
Arrow keys: Move the snake up, down, left, or right.
R: Restart after game over.
Q: Quit the game.
⚠️ Notes
This is a small project for fun and learning.
The game is not for commercial use — all rights for the original Snake belong to Nokia.
(I might change my mind in the future about monetization through Patreon, but currently it’s free.)
📂 Files Included
SnakeGame.py — main game script
snaketheme.mp3 — background music
eat.mp3 — eating sound
crash.mp3 — collision sound
gameover.mp3 — game over sound
💡 Optional Improvements / Future Ideas
Add more levels or obstacles.
Add super apples or poisonous apples like in Snake Remix.
Add visual themes or color customization.
Create a Windows/Linux packaged version with sound included.
