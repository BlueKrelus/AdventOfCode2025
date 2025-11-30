#!/usr/bin/env python3

import os
import re
from pathlib import Path

VERBOSE = True


def v_print(*args, **kwargs):
    if VERBOSE:
        print(*args, **kwargs)


class AdventOfCode:
    def _extract_day_number(self, filepath):
        # Regex Explanation:
        # r"day(\d+)"
        #   - 'day': Matches the literal characters 'day' (case-sensitive)
        #   - '(\d+)': Matches one or more digits (\d+), and puts them into a capturing group ()
        #
        # re.IGNORECASE flag makes it match 'day', 'Day', 'DAY', etc.
        pattern = re.compile(r"day(\d+)", re.IGNORECASE)

        match = pattern.search(filepath)

        if match:
            # Group 1 (the first capturing group) contains the number (\d+)
            return match.group(1)
        else:
            return None

    def __init__(self, script_path):
        self.path = os.path.realpath(script_path)

        v_print(self.path)
        self.day = self._extract_day_number(self.path)

        print(f" ---- Day {self.day} ---- ")

        pass

    def get_input(self, tag: str = ""):
        # Construct the path string based on the day and optional tag
        filename = f"day{self.day}"
        if tag:
            # Note: We only append the tag if it's non-empty (truthy)
            filename = f"day{self.day}_{tag}"

        input_path = Path("./input") / f"{filename}.txt" # Added .txt extension for common use

        if not input_path.exists():
            raise RuntimeError(f"{input_path} doesn't exist")

        try:
            content = input_path.read_text()
            return content
        except Exception as e:
            raise RuntimeError(f"ERROR: Failed to read file {input_path}: {e}")
