from typing import List
"""
power consumption = gamma * epsilon
gamma is most common bits of all power readings
epsilon is least common bits of all power readings, or inverse of gamma

110
101
011

= 111
"""

def read_input(f_name: str = "day3.input") -> List[str]:
    """
    read and format data from day3.input
    """
    with open(f_name, "r") as file_:
        return [line.strip() for line in file_.readlines()]

def part1():
    """
    part 1 of day 3 solution
    """
    nums = read_input()
    gamma = ''
    epsilon = ''
#    nums = ['00100', '11110', '10110', '10111', '10101', '01111', '00111',
#            '11100', '10000', '11001', '00010', '01010',]
    bits = [0 for i in nums[0]]
    #print(bits)

    #place_0 = place_1 = place_2 = place_3 = place_4 = 0
    for num in nums:
        #print(num)
        for index, bit in enumerate(num):
            #print(index, bit)
            bits[index] += int(bit)

    for place in bits:
        gamma = f"{gamma}1" if place >= len(nums) / 2 else f"{gamma}0"

    epsilon = ''.join(['1' if bit == '0' else '0' for bit in gamma])

    print("gamma:", gamma, "decimal:", int(gamma, base=2))
    print("epsilon:", epsilon, "decimal:", int(epsilon, base=2))
    return int(gamma, base=2) * int(epsilon, base=2)

def bit_criteria(nums, index, bit):
    """
    nums - ([str]) Numbers search through
    index - (int) The index in each num of nums to consider
    bit - (str) The bit to compare at num[index]
    """
    return [num for num in nums if num[index] == bit]

def part2():
    """
    life support rating = oxegen generator rating * C02 scrubber rating

    * start by considering first bit, then move on.
    * keep only numbers by 'bit criteria'. disregard those that dont
    * if theres only 1 num left, stop, thats the rating value
    * other wise, move onto next bit

    'bit criteria':
        oxygen: most common value in current position. keep only numbers
        with that bit in that position. If 0/1 equally common, keep values
        with a 1 in the position being considered

        C02: least common value in current bit position. if 0/1 equally
        common, keep values with a 0 in the position being considered
    """
    nums = read_input()
    #nums = ['00100', '11110', '10110', '10111', '10101', '01111', '00111',
    #        '11100', '10000', '11001', '00010', '01010',]

    # Find most common bits in each position
    bits = [0 for i in nums[0]]

    # Now, begin finding oxygen generation ratings(23) and c02 (10)
    tmp = list(nums)
    for index, _ in enumerate(bits):
        zeros = ones = 0
        for num in tmp:
            if num[index] == '0':
                zeros += 1
            else:
                ones += 1

        if ones >= zeros:
            tmp = bit_criteria(tmp, index, '1')
        else:
            tmp = bit_criteria(tmp, index, '0')

        if len(tmp) == 1:
            oxy_rating = tmp[0]
            print(oxy_rating)
            break

    tmp = list(nums)
    for index, _ in enumerate(bits):
        zeros = ones = 0
        for num in tmp:
            if num[index] == '0':
                zeros += 1
            else:
                ones += 1

        if zeros > ones:
            tmp = bit_criteria(tmp, index, '1')
        else:
            tmp = bit_criteria(tmp, index, '0')
        if len(tmp) == 1:
            c02_rating = tmp[0]
            print(c02_rating)
            break

    return int(oxy_rating, base=2) * int(c02_rating, base=2)

if __name__ == "__main__":
    print("part1 answer:", part1())
    print("part2 answer:", part2())
