# Tic Tac Toe Game

## Overview
This project is a graphical implementation of the classic Tic Tac Toe game using Python and Pygame. Players take turns placing their marks ("X" or "O") on a 3x3 grid, aiming to align three marks horizontally, vertically, or diagonally to win the game. The game also supports detecting draws when the grid is filled without a winner.

## Features
- **Graphical Interface**: The game board and player marks are displayed using Pygame.
- **Player Turns**: Alternating turns between two players ("X" and "O").
- **Win Detection**: Checks for horizontal, vertical, and diagonal alignments to determine the winner.
- **Draw Detection**: Displays a draw message if the board is filled without a winner.
- **Score Tracking**: Keeps track of the scores for both players.

## Requirements
- Python 3.x
- Pygame library

## Installation
1. Ensure Python 3.x is installed on your system.
2. Install the Pygame library by running the following command:
   ```bash
   pip install pygame
   ```

## How to Run
1. Clone or download this repository to your local machine.
2. Navigate to the project directory.
3. Run the `main.py` file using Python:
   ```bash
   python main.py
   ```

## Game Controls
- **Mouse Click**: Select a cell to place your mark.
- **ESC Key**: Exit the game.

## File Structure
- `main.py`: The main script containing the game logic.
- `fonts/FreeSansBold.ttf`: Font used for displaying text.
- `images/board.png`: Image of the game board.
- `images/circle.png`: Image representing the "O" player.
- `images/cross.png`: Image representing the "X" player.

## Future Improvements
- Add support for AI opponents.
- Implement a main menu and settings.
- Enhance graphical elements and animations.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it.

## Acknowledgments
- Pygame documentation and community for resources and support.
- Classic Tic Tac Toe game for inspiration.
