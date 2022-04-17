"""
Day 9 looking to evaluate low points in matrix of points

Risk level of a low point is 1 plus it's height

Part1: what is the sum of risk levels of all low points in heightmap?
"""

from typing import List

class LowPoint:
    """
    Dataclass for LowPoints in the Height Map b/c why not seems like it will get
    important in part 2, maybe not
    """
    def __init__(self, row, column, height):
        self._row: int = row
        self._column: int = column
        self._height: int = height
        self._risk: int = height + 1

    @property
    def row(self):
        return self._row

    @property
    def column(self):
        return self._column

    @property
    def height(self):
        return self._height

    @property
    def risk(self):
        return self._risk


def read_file() -> List[List[int]]:
    """
    Read day9.input file and convert from string matrix of data to
    List[List[int]]
    """
    tmp = []
    ret = []
    #with open("day9.test", "r") as input_file:  # example input from adventofcode, used to prototype
    with open("day9.input", "r") as input_file:
        tmp = input_file.readlines()  # gives us ["LINE", "LINE",...]

    for line in tmp:
        ret.append([int(char) for char in line.strip()])  # gives us ret = [[int(2), int(4)...], [...]]

    return ret

def part1() -> int:
    """
    Returns the sum of risk levels for all low points in h_map.

    Low point is locations lower than any of its adjacent locations.
    Adjacent locations are:
        above - row-1, column
        left -  row, column-1
        right - row, column+1
        below - row+1, column

    TODO: incomplete solution, returns 488 which is too high. Return to problem, I imagine issue is
    either with iteration, definition of adjacent, definition of a Low Point, or a fundemental logic
    accident.
    """
    lows = []
    h_map = read_file()
    for r_index, row in enumerate(h_map):
        for c_index, _ in enumerate(row):
            height = h_map[r_index][c_index]

            # Need to perform bounds checking. If outside, then set to 10 so it
            # will not be lower than highest allowed number, 9
            # TODO: see if bounds checking can be cleaner. Can't assume IndexError
            #   saw answers that inserted 10 as a border around and iterated over actual inside

            if r_index - 1 in range(0, len(h_map)):  # range(0, 10) -> 0-9 indexes
                above = h_map[r_index-1][c_index]
            else:
                above = 10

            if c_index - 1 in range(0, len(row)):
                left = h_map[r_index][c_index-1]
            else:
                left = 10

            if c_index + 1 in range(0, len(row)):
                right = h_map[r_index][c_index+1]
            else:
                right = 10

            if r_index + 1 in range(0, len(h_map)):
                below = h_map[r_index+1][c_index]
            else:
                below = 10

            # Want to ensure height is a UNIQUE minimum value from adjacent points
            if height == min(height, above, left, right, below) and height not in [above, left, right, below]:
                #print(f"height: {height}, above: {above}, left: {left}, right: {right}, below: {below}")
                lows.append(LowPoint(r_index, c_index, height))

    return sum([low.risk for low in lows])

if __name__ == "__main__":
    # TODO: incomplete solution, returns 488 which is too high. Return to problem, I imagine issue is
    # either with iteration, definition of adjacent, definition of a Low Point, or a fundemental logic
    # accident.
    print(part1())
