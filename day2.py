#!/usr/bin/env python3

from advent_of_code import AdventOfCode
import re

adc = AdventOfCode(__file__)


class Part1:
    def __init__(self):
        self.invalid_id_sum = 0
        pass

    # def check_repeating(self, ID):
    #     id_str = str(ID)
    #     return re.match(r"^(?P<pattern>\d*)(?P=pattern)$", id_str) is not None

    def check_repeating(self, ID: str):
        id_str = str(ID)
        # print(id_str)
        # print(len(id_str))
        length = len(id_str)
        # assuming repeating pattern need even number of characters
        if length % 2 != 0:
            return False
        if length == 2:
            part_a = id_str[0]
            part_b = id_str[1]
        else:
            # print(length/2)
            part_a = id_str[: int(length / 2)]
            part_b = id_str[int(length / 2) :]
        # print(f"{part_a} -- {part_b}")
        if part_a == part_b:
            return True
        return False

    def check_range(self, start: int, stop: int):
        print(f"Checking range {start} - {stop}")
        for id in range(start, stop + 1):
            if self.check_repeating(id):
                # print(f"----> invalid id {id}")
                self.invalid_id_sum += id

    def run(self):
        # input = adc.get_input("test")
        input = adc.get_input()
        # print(input)
        print("Running")

        range_list = input.split(",")
        # print(range_list)

        for r in range_list:
            start = int(r.split("-")[0])
            stop = int(r.split("-")[1])
            self.check_range(start, stop)
        print("--------")
        print(f"Total sum of invalid id: {self.invalid_id_sum}")


class Part2:
    def __init__(self):
        self.invalid_id_sum = 0
        pass

    def check_repeating(self, ID):
        id_str = str(ID)
        return re.match(r"^(?P<pattern>\d*)(?P=pattern)+$", id_str) is not None

    def check_range(self, start: int, stop: int):
        print(f"Checking range {start} - {stop}")
        for id in range(start, stop + 1):
            if self.check_repeating(id):
                # print(f"----> invalid id {id}")
                self.invalid_id_sum += id

    def run(self):
        # input = adc.get_input("test")
        input = adc.get_input()
        # print(input)
        print("Running")

        range_list = input.split(",")
        # print(range_list)

        for r in range_list:
            start = int(r.split("-")[0])
            stop = int(r.split("-")[1])
            self.check_range(start, stop)
        print("--------")
        print(f"Total sum of invalid id: {self.invalid_id_sum}")


if __name__ == "__main__":
    # part1 = Part1()

    # part1.run()

    part2 = Part2()

    part2.run()
