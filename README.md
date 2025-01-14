# Game of Life Simulation

## Project Overview
This project implements Conway's Game of Life, a zero-player game that simulates cellular automata. The simulation evolves over discrete time steps, following a simple set of rules to determine whether cells live, die, or are born. The application is built using Python and Pygame, providing an interactive visual representation of the game.

---

## Features
- **Random Initialization**: Start the simulation with a randomly generated board.
- **Resizable Window**: Adjust the game window dynamically, with the board extending as needed to fit the new dimensions.
- **Dynamic Evolution**: Watch the cells evolve over time, based on the rules of Conway's Game of Life.
- **Customizable Grid Size**: Modify the initial width and height of the grid to explore different board dimensions.
- **Frame Control**: The simulation runs at a controlled frame rate for smooth visualization.

---

## How to Run
### Prerequisites
- Python 3.x
- Pygame library (install using `pip install pygame`)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Jacob-Mannix/Game-of-Life.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Game-of-Life
   ```
3. Run the game:
   ```bash
   python game_of_life.py
   ```

---

## Rules of the Game
1. **Underpopulation**: A live cell with fewer than two live neighbors dies.
2. **Overpopulation**: A live cell with more than three live neighbors dies.
3. **Survival**: A live cell with two or three live neighbors lives to the next generation.
4. **Reproduction**: A dead cell with exactly three live neighbors becomes a live cell.

---

## Code Highlights
- **Board Initialization**: The board is randomly populated with cells in alive or dead states.
- **Neighbor Count**: Efficient calculation of the number of live neighbors for each cell.
- **Resizable Board**: Dynamically adjusts the board size when the window is resized.
- **Visual Representation**: Uses Pygame to draw the grid and represent cell states.

---

## Future Enhancements
- Add a manual grid editor for customizing initial conditions.
- Enable saving and loading of board states.
- Implement additional cellular automata rules for variation.
- Introduce color-coded states for different stages of cell life.

---

## Author
**Jacob Mannix**  
Graduate, Bachelor of Computer Science  
Florida State University
