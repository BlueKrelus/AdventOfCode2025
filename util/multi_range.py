#!/usr/bin/env python3
from pprint import pprint


class MultiRange:
    def __init__(self) -> None:
        self.range_list: list[tuple[int, int]] = list()
        pass

    def _check_overlap(self, ra: tuple[int, int], rb: tuple[int, int]) -> bool:
        return ra[0] <= rb[1] and rb[0] <= ra[1]

    def _combine(self, ra: tuple[int, int], rb: tuple[int, int]) -> tuple[int, int]:
        new_start = min(ra[0], rb[0])
        new_stop = max(ra[1], rb[1])
        return (new_start, new_stop)

    def _compact(self):
        if len(self.range_list) <= 1:
            return

        def thing(self):
            for i in range(1, len(self.range_list)):
                a = self.range_list[i - 1]
                b = self.range_list[i]

                if self._check_overlap(a, b):
                    self.range_list[i] = self._combine(a, b)
                    self.range_list.pop(i - 1)
                    return True
            return False

        while thing(self):
            pass
            # print("Compacting")

    def add(self, r: tuple[int, int]):
        # print(f"--> adding {r}")
        self.range_list.append(r)
        self._sort()
        self._compact()
        # self.print()

    def _sort_key(self, r):
        return r[0]

    def _sort(self):
        self.range_list.sort(key=self._sort_key)

    def __len__(self) -> int:
        # print("##############")
        length = 0
        for r in self.range_list:
            l = len(range(r[0], r[1] + 1))
            length += l
            # print(f"Length of {r} is {l}")
        return length

    def print(self):
        pprint(self.range_list)
