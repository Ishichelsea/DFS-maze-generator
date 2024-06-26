The provided Python code outlines a Depth-First Search (DFS) algorithm for generating a maze. Here's a concise explanation of how the code works, broken down into key points:

Grid Class Definition:

The Grid class models a maze using a 2D list (self.walls). 1 represents walls and 0 represents open pathways.
The grid size is determined by height and width, which must be odd numbers. The maze generation process uses these dimensions to ensure a border of walls and odd indices for open paths and walls.
Initialization:

In the Grid constructor, the entire grid is initialized with walls (1s). The grid ensures that all elements start as walls which the DFS will later carve into paths.
Utility Functions in Grid:

is_visited(): Checks if a node (cell) is a pathway (0).
set_visited(): Sets a cell to a pathway.
out_of_grid(): Ensures that a given node is within the grid boundaries.
get_unvisited_neighbours(): Determines unvisited neighbor cells that the DFS can move to next, skipping one cell to ensure walls remain between paths.
remove_wall(): Converts a wall between two cells into a path when moving from one cell to the next.
DFS Maze Generation (build_maze_grid_dfs Function):

The function initializes a grid and starts the maze generation from the top-left of the grid (position (1, 1)).
The recursive_backtracking function marks the current position as visited and recursively explores unvisited neighbors by randomly selecting one, removing the wall between the current and chosen cell, and continuing the process from the chosen cell.
Maze Display Function (display_maze_graphically):

Utilizes the Pygame library to visually render the maze. Each cell of the grid is displayed, with walls in green and paths in a brown background.
The display is updated after all cells are drawn, and the program pauses until the user presses Enter.
Execution and Output:

The script initializes the maze generation with specific dimensions, generates the maze, prints it in a textual format, and optionally displays it graphically if Pygame is installed and the last part of the code is run.
This code effectively demonstrates a practical application of the DFS algorithm in maze generation, providing both a logical structure and a graphical representation of the maze.
