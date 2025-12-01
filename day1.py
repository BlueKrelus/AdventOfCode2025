#!/usr/bin/env python3

from advent_of_code import AdventOfCode

adc = AdventOfCode(__file__)


class Part1:
    def __init__(self):
        pass
        self.dial_start = 50
        self.dial_size = 100
        self.dial = self.dial_start

    def turn_dial(self, cmd):
        dir = cmd[0]
        turns = int(cmd[1:])
        # print(dir)
        # print(turns)
        if dir == "L":
            self.dial = self.dial - turns
        else:
            self.dial = self.dial + turns
        self.dial = self.dial % self.dial_size
        print(f"{cmd} --> dial at {self.dial}")

    def run(self):
        print("Running")
        # input = adc.get_input("test")
        input = adc.get_input()

        cmd_list = input.split()

        zero_count = 0

        for c in cmd_list:
            self.turn_dial(c)
            if self.dial == 0:
                zero_count += 1

        print("--------")
        print(f"Number of times at zero: {zero_count}")
        # print(input)


class Part2:
    def __init__(self):
        pass
        self.dial_start = 50
        self.dial_size = 100
        self.dial = self.dial_start
        self.zero_count = 0

    def turn_dial_one_step(self, dir):
        turns = 1
        if dir == "L":
            self.dial = self.dial - turns
        else:
            self.dial = self.dial + turns
        self.dial = self.dial % self.dial_size
        # print(f"{dir} --> dial at {self.dial}")

    def turn_dial(self, cmd):
        dir = cmd[0]
        turns = int(cmd[1:])
        # print(dir)
        # print(turns)
        for _ in range(turns):
            self.turn_dial_one_step(dir)
            if self.dial == 0:
                # print("yay")
                self.zero_count += 1
        # self.dial = self.dial % self.dial_size
        print(f"{cmd} --> dial at {self.dial}")

    def run(self):
        print("Running")
        # input = adc.get_input("test")
        # input = adc.get_input("test2")
        input = adc.get_input()

        cmd_list = input.split()

        # zero_count = 0

        for c in cmd_list:
            self.turn_dial(c)
            # if self.dial == 0:
            #     self.zero_count += 1

        print("--------")
        print(f"Number of times at zero: {self.zero_count}")


if __name__ == "__main__":
    # part1 = Part1()

    # part1.run()

    part2 = Part2()

    part2.run()
