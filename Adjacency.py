# Graph TA coverage using adjacency matrix

import itertools

class Matrix:
    def __init__(self):
        self._matrix = []

    def read_file(self, fp):
        num_rooms = int(fp.readline().strip())
        self._matrix = [set() for _ in range(num_rooms)]

        for line in fp:
            parts = line.strip().split()
            if len(parts) == 2:
                i, j = int(parts[0]) - 1, int(parts[1]) - 1
                self._matrix[i].add(j)
                self._matrix[j].add(i)

    def __str__(self):
        result = []
        for i, neighbors in enumerate(self._matrix):
            line = f"{i+1}: " + " ".join(str(n+1) for n in sorted(neighbors))
            result.append(line)
        return "\n".join(result)

    def adjacent(self, room):
        return self._matrix[room]

    def rooms(self):
        return len(self._matrix)

def open_file():
    while True:
        try:
            fname = input("Enter a file name: ")
            return open(fname, 'r')
        except FileNotFoundError:
            print("File not found. Try again.")

def all_covered(matrix, ta_rooms):
    covered = set()
    for room in ta_rooms:
        covered.add(room)
        covered |= matrix.adjacent(room)
    return covered == set(range(matrix.rooms()))

def main():
    fp = open_file()
    matrix = Matrix()
    matrix.read_file(fp)
    total_rooms = matrix.rooms()

    for num_TAs in range(1, total_rooms + 1):
        for combo in itertools.combinations(range(total_rooms), num_TAs):
            if all_covered(matrix, combo):
                ta_rooms = sorted([r + 1 for r in combo])  # Convert to 1-based
                print(f"TAs needed: {num_TAs}")
                print("TAs assigned to rooms:", ", ".join(map(str, ta_rooms)))
                print("\nAdjacency Matrix:")
                print(matrix)
                return

if __name__ == "__main__":
    main()