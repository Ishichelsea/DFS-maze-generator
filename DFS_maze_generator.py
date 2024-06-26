import random
class Grid(object):
    # Helper class to represent a maze array as a nested list of 1s and 0s
    # For example, a maze could be represented as
    #[[1, 1, 1, 1, 1, 1, 1, 1, 1],
    # [1, 0, 1, 0, 0, 0, 0, 0, 1],
    # [1, 0, 1, 1, 1, 1, 1, 0, 1],
    # [1, 0, 0, 0, 1, 0, 0, 0, 1],
    # [1, 1, 1, 0, 1, 0, 1, 0, 1],
    # [1, 0, 0, 0, 0, 0, 1, 0, 1],
    # [1, 1, 1, 1, 1, 1, 1, 1, 1]]
    # Here the 1s represent walls and the 0s represent corridors.
    # The coordinate system is such that (0,0) is the top-left corner
    # with y increasing downwards.
    
    def __init__(self, height, width):
        assert height%2==1 and width%2==1,"Must have odd height and width"
        assert height>=3 and width>=3,"Width, height too small"
        self.height=height
        self.width=width
        # Initialise the maze as all solid walls (all 1s).
        # The DFS algorithm should carve out the corridors with zeroes
        self.walls=[[1 for x in range(width)] for y in range(height)] 
        self.direction_vectors = {'up':(0,-1),'down': (0,1), 'left':(-1,0), 'right': (1,0)}

    def is_visited(self, node):
        (x,y)=node
        return self.walls[y][x]==0 # With the DFS algorithm, visiting a node always makes it a corridor

    def set_visited(self, node):
        (x,y)=node
        self.walls[y][x]=0  # With the DFS algorithm, visiting a node always makes it a corridor
    
    def out_of_grid(self, node):
        (x,y)=node
        # identify if (x,y) is out of the maze boundary
        return x<0 or x>=self.width or y<0 or y>=self.height

    def get_unvisited_neighbours(self, current_node):
        #returns a list of neighbouring nodes adjacent to current_node
        (x,y)=current_node
        neighbours = []
        for _,dir1 in self.direction_vectors.items():
            (dx,dy)=dir1
            potential_neighbour_node = (x+dx*2,y+dy*2)#we need the *2 here because there is potentially a wall between any two genuine cells of the maze.
            if not self.out_of_grid(potential_neighbour_node):
                if not self.is_visited(potential_neighbour_node):
                    neighbours.append(potential_neighbour_node)
        return neighbours

    def remove_wall(self, current_node, other_node):
        # We want to remove the wall connecting current_node directly to other_node.
        # It is assumed that the other cell is immediately adjacent to this cell (i.e. a distance 2 apart)
        # Hence the connecting wall will be the midpoint of the two nodes.
        (cx,cy)=current_node
        (ox,oy)=other_node
        self.walls[(cy+oy)//2][(cx+ox)//2]=0 # calculates mid-point node, and sets it to zero (no wall)

    def __str__(self):
        return '\n'.join([''.join(str(x)) for x in self.walls])   
        
def build_maze_grid_dfs(n_rows, n_columns):
    layout = Grid(n_rows * 2 + 1, n_columns * 2 + 1)

    def recursive_backtracking(current_position):
        layout.set_visited(current_position)
        Near_By = layout.get_unvisited_neighbours(current_position)

        while Near_By:
            next_position = random.choice(Near_By)
            layout.remove_wall(current_position, next_position)
            recursive_backtracking(next_position)
            Near_By = layout.get_unvisited_neighbours(current_position)

    recursive_backtracking((1, 1))
    return layout

def display_maze_graphically(walls):
    import pygame
    pygame.init()
    display_cell_size=15
    green = (0,155,0)
    brown = (205,133,63)    
    display_width = len(walls[0])*display_cell_size
    display_height = len(walls)*display_cell_size

    pygame.display.set_caption("Maze_viewer")
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    gameDisplay.fill((brown))
    for y,row_of_cells in enumerate(walls):
        for x, cell in enumerate(row_of_cells):
            if cell==1:
                pygame.draw.rect(gameDisplay, green, pygame.Rect(x*display_cell_size, y*display_cell_size, display_cell_size-1,display_cell_size-1))
    pygame.display.flip()
    input("Press enter")


size_x=8
size_y=10
maze_grid = build_maze_grid_dfs(size_y, size_x)
print("Generated Maze:")
print(maze_grid)

# This next display method displays the maze graphically:
# To get graphical displayer to run, you need to have pygame installed.
# e.g. pip install pygame
# or on Ubuntu, sudo apt install python-pygame
display_maze_graphically(maze_grid.walls)
