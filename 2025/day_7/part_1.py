import random
import time

from rich.live import Live
from rich.text import Text



with open("day_7_input_test.txt") as f:
    grid: list = [list(line.rstrip()) for line in f]
    



def generate_grid(grid: list) -> Text:
    """Make a new table."""
    text = Text()
    
    for row in grid:
        text.append(''.join(row) +'\n')
    return text


with Live(generate_grid(grid), refresh_per_second=10) as live:
    for i, row in enumerate(grid[:-1]):
        time.sleep(.1)

        if row[0] == '.' or row[0] == '|':
            grid[i+1][0] = '|'

        # grid[i+1] = row

        live.update(generate_grid(grid))