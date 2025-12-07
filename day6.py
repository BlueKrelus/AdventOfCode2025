#!/usr/bin/env python3

from advent_of_code import AdventOfCode
from pprint import pprint

adc = AdventOfCode(__file__)


class Part1:
    def __init__(self):
        self.math_matrix: list[list[int]] = list()
        self.math_operations: list[str] = list()
        self.grand_total = 0

    def do_operation(self, x_index: int, operation: str):
        my_problem = operation.join(
            [str(x) for x in [v[x_index] for v in self.math_matrix]]
        )
        print(my_problem, end="")
        result = eval(my_problem)
        print(f"={result}")
        self.grand_total += result

    def run(self):
        print("Running")
        data = adc.get_input()
        # data = adc.get_input("test")

        for l in data.split("\n"):
            if "+" in l:
                self.math_operations = l.split()
            else:
                numbers = [int(x) for x in l.split(" ") if len(x.strip()) > 0]
                if numbers:
                    self.math_matrix.append(numbers)
        # pprint(self.math_matrix)
        # pprint(self.math_operations)

        for i, operation in enumerate(self.math_operations):
            self.do_operation(i, operation)
        print("--------")
        print(f"Grand Total: {self.grand_total}")


class Part2:
    def __init__(self):
        self.math_matrix: list[list[int]] = list()
        self.math_operations: list[str] = list()
        self.grand_total = 0

    def do_operation(self, x_index: int, operation: str):
        my_problem = operation.join([str(x) for x in self.math_matrix[x_index]])
        print(my_problem, end="")
        result = eval(my_problem)
        print(f"={result}")
        self.grand_total += result

    def run(self):
        print("Running")
        data = adc.get_input()
        # data = adc.get_input("test")

        print(data)
        self.pre_matrix = list()
        for l in data.split("\n"):
            if "+" in l:
                self.math_operations = l.split()
            if any(c.isdigit() for c in l):
                self.pre_matrix.append(l)
            else:
                pass  # :-)
        pprint(self.pre_matrix)
        # pprint(self.math_operations)
        #
        # matrix_index = 0
        self.math_matrix.append(list())
        for x in reversed(range(len(self.pre_matrix[0]))):
            # print(x)
            try:
                value = int("".join([t[x] for t in self.pre_matrix]))
                print(value)
                self.math_matrix[-1].append(value)
            except Exception:
                self.math_matrix.append(list())
        pprint(self.math_matrix)
        # exit()
        for i, operation in enumerate(reversed(self.math_operations)):
            self.do_operation(i, operation)
            # break
        print("------")
        print(f"Grand Total: {self.grand_total}")


if __name__ == "__main__":
    # part1 = Part1()

    # part1.run()

    part2 = Part2()

    part2.run()
