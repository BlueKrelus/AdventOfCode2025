#!/usr/bin/env python3

from advent_of_code import AdventOfCode

adc = AdventOfCode(__file__)


class Part1:
    def __init__(self):
        pass

    def run(self):
        input = adc.get_input()
        print(input)
        print("Running")


class Part2:
    def __init__(self):
        pass

    def run(self):
        input = adc.get_input(tag="part2")
        print(input)
        print("Running")


if __name__ == "__main__":
    part1 = Part1()

    part1.run()

    part2 = Part2()

    part2.run()
