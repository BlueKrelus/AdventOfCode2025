#!/usr/bin/env python3

from advent_of_code import AdventOfCode

adc = AdventOfCode(__file__)


class Part1:
    def __init__(self):
        self.cords_list = list()
        pass

    def calc_area(self, point_a: list[int], point_b: list[int]):
        x1 = point_a[0]
        y1 = point_a[1]
        x2 = point_b[0]
        y2 = point_b[1]

        height = (y1 - y2 if y1 > y2 else y2 - y1) + 1
        width = (x1 - x2 if x1 > x2 else x2 - x1) + 1
        return height * width

    def run(self):
        data = adc.get_input()
        # data = adc.get_input("test")
        print(data)
        print("Running")

        for c in data.split():
            print(c.split())
            self.cords_list.append([int(x) for x in c.strip().split(",")])
        print(self.cords_list)

        max_area = 0

        for c1 in self.cords_list:
            for c2 in self.cords_list:
                area = self.calc_area(c1, c2)
                if area > max_area:
                    max_area = area
                    print(f"max area {c1} {c2}: {max_area}")


class Part2:
    def __init__(self):
        pass

    def run(self):
        data = adc.get_input()
        print(data)
        print("Running")


if __name__ == "__main__":
    part1 = Part1()

    part1.run()

    # part2 = Part2()

    # part2.run()
