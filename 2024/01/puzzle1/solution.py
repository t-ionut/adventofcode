#!/usr/bin/env python
"""
How to run it:

python solution.py input.txt
"""

import sys

if __name__ == "__main__":
    file_input = sys.argv[1]

    list_a = []
    list_b = []
    distance_sum = 0

    with open(file_input, "r") as f:
        cursor_pos = f.tell()
        line = f.readline()
        while cursor_pos != f.tell():
            if line:
                [location_id_a, location_id_b] = line.strip().split("   ")
                list_a.append(int(location_id_a))
                list_b.append(int(location_id_b))
            cursor_pos = f.tell()
            line = f.readline()

    list_a = list(sorted(list_a))
    list_b = list(sorted(list_b))

    for idx, num in enumerate(list_a):
        distance_sum += abs(num - list_b[idx])

    print(f"Total sum of distances: {distance_sum}")

