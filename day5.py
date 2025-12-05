#!/usr/bin/env python3

from advent_of_code import AdventOfCode
from pprint import pprint

adc = AdventOfCode(__file__)


class Part1:
    def __init__(self):
        self.fresh_ranges=list()
        self.ingredient_IDs=list()
        pass

    def check_if_fresh(self,id):
        for r in self.fresh_ranges:
            if id in range(r[0],r[1]+1):
                return True
        return False

    def run(self):
        data = adc.get_input()
        # data = adc.get_input("test")
        # print(data)
        print("Running")
        data = data.split("\n\n")
        for r in data[0].split('\n'):
            ra = [int(x) for x in r.strip().split('-')]
            # print(ra)
            self.fresh_ranges.append(ra)
        pprint(self.fresh_ranges)
        # pprint(data[1])
        self.ingredient_IDs = [int (x ) for x in data[1].split()]
        pprint(self.ingredient_IDs)

        num_fresh = 0
        for id in self.ingredient_IDs:
            if self.check_if_fresh(id):
                print(f"Id {id}, is fresh!!!!!")
                num_fresh += 1
            else:
                print(f"Id {id}, is not fresh :-(")
        print("--------")
        print(f"Total fresh ingredients: {num_fresh}")

class Part2:
    def __init__(self):
        self.fresh_ranges=list()
        self.ingredient_IDs=list()
        pass

    def check_if_fresh(self,id):
        for r in self.fresh_ranges:
            if id in range(r[0],r[1]+1):
                return True
        return False

    def run(self):
        data = adc.get_input()
        # data = adc.get_input("test")
        # print(data)
        print("Running")
        data = data.split("\n\n")
        for r in data[0].split('\n'):
            ra = [int(x) for x in r.strip().split('-')]
            # print(ra)
            self.fresh_ranges.append(ra)
        # pprint(self.fresh_ranges)
        # pprint(data[1])
        self.ingredient_IDs = [int (x ) for x in data[1].split()]
        # pprint(self.ingredient_IDs)

        # num_fresh = 0
        all_fresh_IDs = set()
        for r in self.fresh_ranges:
            print(r)
            for i in range(r[0],r[1]+1):
                all_fresh_IDs.add(i)
                if i % 100 == 0:
                    print(i)
        print("--------")
        pprint(all_fresh_IDs)
        print(f"Total fresh ingredients IDs: {len(all_fresh_IDs)}")

if __name__ == "__main__":
    part1 = Part1()

    part1.run()

    # part2 = Part2()

    # part2.run()
