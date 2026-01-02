import random
import time


INPUT_FILE: str = '../../advent_of_code_inputs/2025/day7/day_7_input.txt'
# INPUT_FILE: str = '../../advent_of_code_inputs/2025/day7/day_7_input_test.txt'


# Read file
with open(INPUT_FILE) as f:
    grid: list = [list(line.rstrip()) for line in f]

# Track Timelines
timeline_tracker: list = [0]*len(grid[0])

for i, row in enumerate(grid):

    if 'S' in row:
        s_idx: int = row.index('S')
        timeline_tracker[s_idx] = 'S'
        continue
    else:

        for idx, val in enumerate(row):
            if timeline_tracker[idx] == 'S':
                timeline_tracker[idx-1] = 1
                timeline_tracker[idx+1] = 1
                timeline_tracker[idx] = 0
                continue

            elif val == '^':
                timeline_tracker[idx-1] += timeline_tracker[idx]
                timeline_tracker[idx+1] += timeline_tracker[idx]
                timeline_tracker[idx] = 0
                

print(f'Total timelines: {sum(timeline_tracker)}')