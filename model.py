from mesa import Model
from mesa.time import SimultaneousActivation
from mesa.space import Grid

from .cell import Cell


class ConwaysGameOfLife(Model):
    """
    Represents the 2-dimensional array of cells in Conway's
    Game of Life.
    """
def __init__(self, height=50, width=50):
        """
        Create a new playing area of (height, width) cells.
        """

        # Set up the grid and schedule.
