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

def merge2(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # create a line initialized w zeros the length of given line
    merged_line = [0] * len(line)
    # set the counter
    merge_idx = 0
    # simple iteration gives us the value. Compare it.
    for value in line:
        if value:
            # if we don't get a zero, set the value
            if not(merged_line[merge_idx]):
                merged_line[merge_idx] = value
            # if the line
            elif value == merged_line[merge_idx]:
                merged_line[merge_idx] *= 2
                merge_idx+=1
            else:
                merge_idx+=1
                merged_line[merge_idx] = value            
    return merged_line           


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._height = grid_height
        self._width = grid_width
        self._goal = 2048
        self._won = False
        
        self._grid = [[0 for col in xrange(self.get_grid_width())] for row in range(self.get_grid_height())]

        self._initial_tiles = {UP: [(0,col) for col in xrange(grid_width)],
                              DOWN: [(grid_height-1,col) for col in xrange(grid_width)],
                              LEFT: [(row,0) for row in xrange(grid_height)],
                              RIGHT: [(row, grid_width-1) for row in xrange(grid_height)]}
                         
        # Initialize a dict for row / col line lengths for each move direction (used by move() method)
        self._line_lengths = {UP: grid_height,
                             DOWN: grid_height,
                             LEFT: grid_width,
                             RIGHT: grid_width}
        #  reset game w two random tiles on new board
        self.reset()
        
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        self._grid = [[0 for dummy_col in xrange(self.get_grid_width())] for dummy_row in range(self.get_grid_height())]
        # generate 2 random tiles
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        printable_str = ""
        for row in self._grid:
            printable_str += str(row) + "\n"
        return printable_str

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
        same_tiles = True
        
        for init_tile in self._initial_tiles[direction]:
            # build line to feed to merge() from a line or col (direction dependent)
            # [ get_tile function for idx in iterator ]
            line = [self.get_tile(init_tile[0]+idx*OFFSETS[direction][0],
                             init_tile[1] + idx * OFFSETS[direction][1])
                    for idx in range(self._line_lengths[direction])]
            
           
            # Run merge function on line
            new_line = merge(line)
            
            # check for changes
            same_tiles = same_tiles and (new_line == line)
            
            # set new values
            for idx in xrange(self._line_lengths[direction]):
                self.set_tile(init_tile[0] + idx * OFFSETS[direction][0],
                              init_tile[1] + idx * OFFSETS[direction][1],
                             new_line[idx])
                
        if not same_tiles:
            self.new_tile()
                    
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
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        #print self.grid
        return self._grid[row][col]
    
    def get_empty_tiles(self):
        """
        Return an (x,y) pair for each empty cell
        """
        return [(row, col) for col in xrange(self.get_grid_width())
                for row in xrange(self.get_grid_height())

                if self.get_tile(row,col) == 0]


# for running in http://www.codeskulptor.org w gui
poc_2048_gui.run_gui(TwentyFortyEight(2, 2))

