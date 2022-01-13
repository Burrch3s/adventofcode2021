from typing import List

"""
It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:

forward X increases the horizontal position by X units.
down X increases the depth by X units.
up X decreases the depth by X units.
Note that since you're on a submarine, down and up affect your depth, and so they have the opposite result of what you might expect.
"""

class Submarine:
    def __init__(self, start_x: int = 0, start_y: int = 0, start_aim: int = 0):
        self.x = start_x
        self.depth = start_y
        self.aim = start_aim

    def forward(self, num):
        """
        move forward. X axis
        """
        self.x += num
        self.depth += (self.aim * num)

    def up(self, num):
        """
        move up. Y axis
        """
        #self.depth -= num
        self.aim -= num

    def down(self, num):
        """
        move down. Y axis
        """
        #self.depth += num
        self.aim += num

def read_input(file_name: str = "day2.input") -> List:
    """reads file name and outputs to expected format"""
    ret = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            tmp = line.split(' ')
            ret.append([tmp[0], int(tmp[1])])

    return ret

def part1():
    """
    plot basic course for sub and do something with it at end
    """
    #course = [['forward', 5], ['down', 5], ['forward', 8], ['up', 3], ['down', 8], ['forward', 2]]
    course = read_input()
    sub = Submarine()

    for move, num in course:
        func = getattr(sub, move)
        func(num)

    print("sub position:", sub.x, sub.depth)
    return sub.x * sub.depth

def part2():
    """
    include aim into sub movement
    """
    #course = [['forward', 5], ['down', 5], ['forward', 8], ['up', 3], ['down', 8], ['forward', 2]]
    course = read_input()
    sub = Submarine()

    for move, num in course:
        func = getattr(sub, move)
        func(num)

    print("sub position:", sub.x, sub.depth, sub.aim)
    return sub.x * sub.depth

if __name__ == "__main__":
    #print("part1 answer:", part1())
    print("part2 answer:", part2())
