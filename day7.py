#!/usr/bin/env python3

from advent_of_code import AdventOfCode

adc = AdventOfCode(__file__)

BEAM='|'
START='S'

class Part1:
    def __init__(self):
        self.data : list[str] = list()
        self.splits = 0
        pass

    def iterate(self,prev_line:str, current_line:str):
        result = list(current_line)
        for i,c in enumerate(prev_line):
            match c:
                case '|' | 'S' if result[i] == '^':
                    result[i-1] = BEAM
                    result[i+1] = BEAM
                case '|' | 'S':
                    result[i] = BEAM
                case _:
                    pass

        # self.splits += result.
        return "".join(result)

        pass
    def run(self):
        # self.data = adc.get_input()
        self.data = adc.get_input("test")
        print("Running")
        self.data = self.data.split('\n')
        print(self.data)
        for i, _ in enumerate(self.data):
            print(i)
            # print(line)
            try:
                self.data[i+1] = self.iterate(self.data[i], self.data[i+1])
            except Exception as e:
                print(e)
            print(self.data[i])

        print("########")
        for line in self.data:
            print(line)


        print("########")
        print(f"splits {self.splits}")

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
