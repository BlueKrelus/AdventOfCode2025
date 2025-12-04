class NegList(list):
    def __getitem__(self, n):
        if n < 0:
            raise IndexError("...")
        return list.__getitem__(self, n)


class Grid:
    def __init__(self):
        self.matrix = list()
        self.width = 0
        self.height = 0

    def load(self, data: str):
        self.matrix = list()
        for line in data.split():
            self.matrix.append(NegList(line.strip()))
        self.width = len(self.matrix[0])
        self.height = len(self.matrix)

    def get(self, x, y):
        if y < 0 or x < 0:
            return "?"

        return self.matrix[y][x]

    def set(self, x, y, c):
        self.matrix[y][x] = c

    def print(self):
        for l in self.matrix:
            print(f"{"".join(l)}")

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

    def remove_all(self, c, replace_with=None):
        for y, m in enumerate(self.matrix):
            for x, _ in enumerate(m):
                if self.matrix[y][x] == c:
                    if replace_with:
                        self.matrix[y][x] = replace_with
                    else:
                        self.matrix[y][x] = "."
