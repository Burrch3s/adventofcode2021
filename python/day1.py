from typing import List

"""
The first order of business is to figure out how quickly the depth increases, just so you know what you're dealing with - you never know if the keys will get carried into deeper water by an ocean current or a fish or something.

To do this, count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.)

example

199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)


Question:

In this example, there are 7 measurements that are larger than the previous measurement.

How many measurements are larger than the previous measurement?
"""

def read_input(nums: str = "day1.input") -> List[int]:
    """
    read file and return as ints
    """
    with open(nums, "r") as f:
        return [int(line) for line in f.readlines()]

def part1() -> int:
    """
    Count number of times a depth measurment increases from previous measurement
    """
    nums = read_input()
    #  nums = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]  #  <<< testing
    count = 0  # num of measurements that increases from previous
    for index, num in enumerate(nums):
        prev = index - 1
        if prev < 0:
            continue

        count = count + 1 if nums[prev] < num else count

    return count

def part2() -> int:
    """
    Your goal now is to count the number of times the sum of measurements in this sliding window increases from the previous sum.

    So, compare A with B, then compare B with C, then C with D, and so on.

    Stop when there aren't enough measurements left to create a new three-measurement
    """
    nums = read_input()
    #nums = [607, 618, 618, 617, 647, 716, 769, 792]
    total_nums = len(nums)
    count = 0  # num of 3-measurement window sum increases

    for index, num in enumerate(nums):
        # Skip comparing previous 3-measurement window on first element
        prev = index - 1
        if prev < 0:
            continue

        # Break loop when not enough nums for 3-window sum
        if index == total_nums - 2:
            break

        prev_sum = nums[prev] + nums[index] + nums[index+1]
        curr_sum = nums[index] + nums[index + 1] + nums[index + 2]
        count = count + 1 if prev_sum < curr_sum else count

    return count

if __name__ == "__main__":
    print(part1())
    print(part2())
