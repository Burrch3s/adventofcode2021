from typing import List


def read_input(nums: str = "day6.input") -> List[int]:
    """
    read file and return as ints
    """
    with open(nums, "r") as f:
        return [int(item) for item in f.read().strip().split(',')]

class Fish:
    def __init__(self, time):
        self.time = time

class Pool:
    def __init__(self, fish):
        self.fish_count = len(fish)
        self.fish = [Fish(time) for time in fish]

    def day(self):
        # update fish
        tmp = list(self.fish)
        for fish in tmp:
            if fish.time == 0:
                fish.time = 6
                self.fish.append(Fish(8))
            else:
                fish.time -= 1

        # update fish count
        self.fish_count = len(self.fish)


def part1():
    #pool = Pool([3, 4, 3, 1, 2])
#    for _ in range(26):
#        pool.day()
    pool = Pool(read_input())
    for _ in range(80):
        pool.day()

    return len(pool.fish)

def part2():
    pool = Pool(read_input())
    for _ in range(256):
        pool.day()

    return len(pool.fish)

if __name__ == "__main__":
    print(part1())
    print(part2())
