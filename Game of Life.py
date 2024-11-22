import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ALIVE_COLOR = (0, 255, 0)  # Green for alive cells

# Set the initial size of the cells
CELL_SIZE = 10

# Create a board state with random 1s (ALIVE) and 0s (DEAD)
def random_state(width, height):
    board_state = [[random.randint(0, 1) for _ in range(width)] for _ in range(height)]
    return board_state

# Function to count live neighbors of a given cell
def count_live_neighbors(board, x, y):
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    
    live_neighbors = 0
    height = len(board)
    width = len(board[0])
    
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        if 0 <= nx < height and 0 <= ny < width:
            live_neighbors += board[nx][ny]
    
    return live_neighbors

# Function to calculate the next state of the board
def next_board_state(board):
    height = len(board)
    width = len(board[0])
    
    new_board = [[0 for _ in range(width)] for _ in range(height)]
    
    for x in range(height):
        for y in range(width):
            live_neighbors = count_live_neighbors(board, x, y)
            
            if board[x][y] == 1:  # Cell is alive
                if live_neighbors < 2 or live_neighbors > 3:
                    new_board[x][y] = 0  # Cell dies
                else:
                    new_board[x][y] = 1  # Cell lives
            else:  # Cell is dead
                if live_neighbors == 3:
                    new_board[x][y] = 1  # Cell becomes alive
    
    return new_board

# Function to draw the board state in the Pygame window
def draw_board(screen, board, cell_size):
    for x in range(len(board)):
        for y in range(len(board[0])):
            color = ALIVE_COLOR if board[x][y] == 1 else WHITE
            pygame.draw.rect(screen, color, pygame.Rect(y * cell_size, x * cell_size, cell_size, cell_size))

def extend_board(board, new_width, new_height):
    current_height = len(board)
    current_width = len(board[0])

    # Extend the height if necessary
    if new_height > current_height:
        for _ in range(new_height - current_height):
            board.append([0] * current_width)

    # Extend the width if necessary
    for row in board:
        if new_width > current_width:
            row.extend([0] * (new_width - current_width))

    return board

def run_game_of_life(width, height):
    # Initialize the Pygame window to be resizable
    screen = pygame.display.set_mode((width * CELL_SIZE, height * CELL_SIZE), pygame.RESIZABLE)
    pygame.display.set_caption("Game of Life")

    # Create the initial random board state
    board = random_state(width, height)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                # Get the new window size and adjust the cell size
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                new_width = event.w // CELL_SIZE
                new_height = event.h // CELL_SIZE
                board = extend_board(board, new_width, new_height)
                width = new_width
                height = new_height

        # Draw the current board state
        draw_board(screen, board, CELL_SIZE)

        # Update the display
        pygame.display.flip()

        # Calculate the next board state
        board = next_board_state(board)

        # Control the frame rate
        time.sleep(0.1)

    pygame.quit()

# Main function to start the game
if __name__ == "__main__":
    width = 80  # Number of cells horizontally
    height = 60  # Number of cells vertically
    run_game_of_life(width, height)
