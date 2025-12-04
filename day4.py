#!/usr/bin/env python3

from advent_of_code import AdventOfCode
from time import sleep
from util.grid import Grid

adc = AdventOfCode(__file__)


class Matrix:
    def __init__(self):
        pass


class Part1:
    def __init__(self):
        self.matrix = list()
        pass

    def get(self, x, y):
        if y < 0 or x < 0:
            return "?"

        return self.matrix[y][x]

    def get_adjecent(self, c, x, y):
        count = 0
        x_offset = [-1, -1, -1, 0, 0, 1, 1, 1]
        y_offset = [-1, 0, 1, -1, 1, -1, 0, 1]
        for x_i, y_i in zip(x_offset, y_offset):
            try:
                if self.get(x + x_i, y + y_i) == c:
                    count += 1
            except Exception:
                continue
        return count

    def run(self):
        # data = adc.get_input()
        data = adc.get_input("test")
        # data = adc.get_input("test2")
        print(data)
        print("Running")
        # print(self.matrix)
        for line in data.split():
            self.matrix.append(line.strip())

        print(self.matrix)

        num_paper_rolls = 0
        for y in range(len(self.matrix)):
            print("")
            for x in range(len(self.matrix[0])):
                c = self.get(x, y)

                if self.get(x, y) == "@" and self.get_adjecent("@", x, y) < 4:
                    num_paper_rolls += 1
                    print("x", end="")
                else:
                    print(self.get(x, y), end="")
                # input("Press enter to continue")
            # break
        print("")
        print(f"Number of accessible: {num_paper_rolls}")


class Part2:
    def __init__(self):
        self.grid = Grid()

    def iterate(self):
        num_paper_rolls = 0
        for y in range(self.grid.height):
            print("")
            for x in range(self.grid.width):
                c = self.grid.get(x, y)
                if self.grid.get(x, y) == "@" and self.grid.get_adjecent("@", x, y) < 4:
                    num_paper_rolls += 1
                    self.grid.set(x, y, "x")

        self.grid.print()
        print(f"Number of accessible: {num_paper_rolls}")
        sleep(0.1)
        return num_paper_rolls

    def run(self):
        data = adc.get_input()
        # data = adc.get_input("test")

        print("Running")
        self.grid.load(data)

        rolls = 0
        val = self.iterate()
        self.grid.remove_all("x")
        rolls += val
        while val > 0:
            val = self.iterate()
            self.grid.remove_all("x")
            rolls += val

        print(f"Total num of removed rolls: {rolls}")


if __name__ == "__main__":
    # part1 = Part1()

    # part1.run()

    part2 = Part2()

    part2.run()
