"""
Clone of 2048 game.
"""
import random
import poc_2048_gui


# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """ 2048 helper function to merge rows """
    
    # deal w one element list
    if len(line) == 1:
        return line
    # create result list w length of given line
    result = [0] * len(line)
    result_pos = 0
    length = xrange(1,len(line))
    
    # collapse the line
    for item in line[:]:
        if item != 0:
            result.insert(result_pos,item)
            result_pos += 1
    result = result[0:len(line)]
    
    # avoid calling len() each time
    for idx in length:
        item = result[idx]
        if item != 0 and item == result[idx - 1]:
            doubled = item * 2
            result[idx - 1] = doubled
            del result[idx]
            result.append(0)
    return result

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._height = grid_height
        self._width = grid_width
        self._goal = 2048
        self._won = False
        
        self.grid = [[0 for col in xrange(self.get_grid_width())] for row in range(self.get_grid_height())]

        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        self.grid = [[0 for col in xrange(self.get_grid_width())] for row in range(self.get_grid_height())]
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return ""

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        pass

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # create the choices list w the above requirement
        choices = [2] * 9 + [4]
        #print choices
        new_tile_val = random.choice(choices)
        
        # now that we have value of new tile, place it in an empty square
        #empty_tiles = self.get_empty_tiles()
        # grab a radom pair of empty tiles
        row, col = random.choice(self.get_empty_tiles())
        
        
        # set the new cell value
        self.set_tile(row, col, new_tile_val)
        

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        #print self.grid
        return self.grid[row][col]
    
    def get_empty_tiles(self):
        """
        Return an (x,y) pair for each empty cell
        """
        return [(row, col) for col in xrange(self.get_grid_width())
                for row in xrange(self.get_grid_height())

                if self.get_tile(row,col) == 0]



#poc_2048_gui.run_gui(TwentyFortyEight(4, 6))
