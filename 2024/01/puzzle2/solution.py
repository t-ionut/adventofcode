#!/usr/bin/env python
"""
How to run it:

python solution.py input.txt
"""

import sys

if __name__ == "__main__":
    file_input = sys.argv[1]

    similarity_scores_a = {}
    occurrences_b = {}
    similarity_score = 0

    with open(file_input, "r") as f:
        cursor_pos = f.tell()
        line = f.readline()
        while cursor_pos != f.tell():
            if line:
                [location_id_a, location_id_b] = [int(num) for num in line.strip().split("   ")]

                similarity_scores_a[location_id_a] = 0

                if location_id_b in occurrences_b:
                    occurrences_b[location_id_b] += 1
                else:
                    occurrences_b[location_id_b] = 1

            cursor_pos = f.tell()
            line = f.readline()

    for key_a in similarity_scores_a:
        similarity_scores_a[key_a] = key_a * occurrences_b.get(key_a, 0)

    print(f"Total similarity score: {sum(similarity_scores_a.values())}")

