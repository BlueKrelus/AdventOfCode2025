#!/usr/bin/env python3

from advent_of_code import AdventOfCode

adc = AdventOfCode(__file__)


class Part1:
    def __init__(self):
        pass

    def find_max_joltage(self, j_line: str):
        max_j = 0

        for a in range(0, len(j_line) - 1):
            for b in range(a + 1, len(j_line)):
                # print(j_line[a:b])
                val = int(f"{j_line[a]}{j_line[b]}")
                max_j = max(max_j, val)
        return max_j

    def run(self):
        print("Running")
        total_max_j = 0
        input = adc.get_input()
        # input = adc.get_input("test")
        # print(input)
        line_list = input.split()
        print(line_list)
        for l in line_list:
            print(f"-- {l} --")
            max_j = self.find_max_joltage(l)
            print(f"Max j: {max_j}")
            total_max_j += max_j
            # break
        print("--------")
        print(f"Total max joltage: {total_max_j}")



class Part2:
    def __init__(self):
        pass


    def remove_one(self, j_line:str):
        max_j = int(j_line[1:])
        print(f":{max_j}")

        # The jank line
        max_j = max(max_j , int(j_line[:-1]))

        print(f":{max_j}")
        for i in range(len(j_line)-1):
            val = int(j_line[:i] + j_line[i+1:])
            print(val)
            max_j = max(max_j, int(val))
        print(f"-- > {max_j}")
        return str(max_j)

    def find_max_joltage(self, j_line: str):
        while len(j_line) > 12:
            j_line = self.remove_one(j_line)
        return int(j_line)

    def run(self):
        print("Running")
        total_max_j = 0
        data = adc.get_input()
        # data = adc.get_input("test")
        # print(input)
        line_list = data.split()
        print(line_list)
        for l in line_list:
            print(f"-- {l} --")
            max_j = self.find_max_joltage(l)
            print(f"Max j: {max_j}")
            total_max_j += max_j
            # input("Press enter for next")
            # break
        print("--------")
        print(f"Total max joltage: {total_max_j}")


if __name__ == "__main__":
    # part1 = Part1()

    # part1.run()

    part2 = Part2()

    part2.run()
