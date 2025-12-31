import random
import time

from rich.live import Live
from rich.text import Text

    
# functions
def generate_grid(grid: list) -> Text:
    text = Text()
    
    for row in grid:
        text.append(''.join(row) +'\n')
    return text


# Read file
# INPUT_FILE: str = "day_7_input_test.txt" 
INPUT_FILE: str = "day_7_input.txt" 

with open(INPUT_FILE) as f:
    grid: list = [list(line.rstrip()) for line in f]

# Render grid
with Live(generate_grid(grid), refresh_per_second=10) as live:
    starting_idx: int = grid[0].index('S')

    previous_row: list = grid[0]
    split_count: int = 0
    for i, row in enumerate(grid[1:]):
        time.sleep(.1)

        if previous_row == grid[0]:
            row[starting_idx] = '|'
            previous_row = row
            continue
        else:
            zipped_rows = zip(previous_row, row)
            
            for i, pair in enumerate(zipped_rows):
                if pair == ('|', '^'):
                    if row[i-1] == '.' or row[i+1] =='.':
                        split_count +=1
                    if row[i-1] == '.':
                        row[i-1] = '|'
                        # split_count += 1
                    if row[i+1] == '.':
                        row[i+1] = '|'
                        # split_count += 1
                elif pair == ('|', '.'):
                    row[i] = '|'

        previous_row = row

        live.update(generate_grid(grid))

print(f'Total splits: {split_count}')