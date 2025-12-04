#!/usr/bin/env python3

from advent_of_code import AdventOfCode

adc = AdventOfCode(__file__)


class Matrix:
    def __init__(self):
        pass


class Part1:
    def __init__(self):
        self.matrix: list[str] = list()
        pass

    def get(self, x, y):
        # if x > len(self.matrix[0]):
        #     x = 0
        # elif x < 0:
        #     x = len(self.matrix[0])

        # if y > len(self.matrix):
        #     y = 0
        # elif y < 0:
        #     y = len(self.matrix)
        # print(f"get {x}:{y}")
        if y<0 or x<0:
            return '?'

        return self.matrix[y][x]


    def get_adjecent(self, c, x, y):
        # print("get_adjecent")
        count = 0
        x_offset = [-1,-1,-1, 0,  0, 1, 1, 1]
        y_offset = [-1, 0, 1,-1,  1,-1, 0, 1]
        # for i in range(len(x_offset)):
        for x_i,y_i in zip(x_offset,y_offset):
            # print(f"{x_i},{y_i}")
            try:
                if self.get(x + x_i, y + y_i) == c :
                    count += 1
            except Exception:
                continue
        # for x_i in range(x - 1, x + 2):
        #     for y_i in range(y - 1, y + 2):
        #         if x_i == x and y_i == y:
        #             continue
        #         print(f"{x_i},{y_i}")
        #         if self.get(x_i, y_i) == c :
        #             count += 1
        # print("----")
        # print(count)
        return count

    def run(self):
        data = adc.get_input()
        # data = adc.get_input("test")
        # data = adc.get_input("test2")
        print(data)
        print("Running")
        print(self.matrix)
        for line in data.split():
            self.matrix.append(line.strip())

        print(self.matrix)
        print(self.matrix[-1][-1])

        num_accesable = 0
        for y in range(len(self.matrix)):
            print("")
            for x in range(len(self.matrix[0])):
                c =self.get(x,y)

                if self.get(x,y) == '@' and self.get_adjecent('@', x, y) < 4:
                # if self.get_adjecent("@", x, y) < 4:
                    num_accesable += 1
                    print('x', end="")
                else:
                    print(self.get(x,y), end="")
                # input("Press enter to continue")
            # break
        print("")
        print(f"Number of accessible: {num_accesable}")


class Part2:
    def __init__(self):
        pass

    def run(self):
        input = adc.get_input()
        print(input)
        print("Running")


if __name__ == "__main__":
    part1 = Part1()

    part1.run()

    # part2 = Part2()

    # part2.run()
