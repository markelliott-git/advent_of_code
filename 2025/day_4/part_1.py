import pandas


def count_rolls(
        grid, i: int, j: int,
        first_row, last_row,
        first_column, last_column
    ):

    count: int = 0

    def up(): return grid[i-1][j]
    def up_right(): return grid[i-1][j+1]
    def right(): return grid[i][j+1]
    def down_right(): return grid[i+1][j+1]
    def down(): return grid[i+1][j]
    def down_left(): return grid[i+1][j-1]
    def left(): return grid[i][j-1]
    def up_left(): return grid[i-1][j-1]

    if i==first_row and j==first_column:
        valid_direction = [right(), down_right(), down()]
    elif i==first_row and j==last_column:
        valid_direction = [left(), down_left(), down()]
    elif i==last_row and j==first_column:
        valid_direction = [up(), up_right(), right()]
    elif i==last_row and j==last_column:
        valid_direction = [left(), up_left(), up()]
    elif i==first_row:
        valid_direction = [right(), down_right(), down(), down_left(), left()]
    elif j==first_column:
        valid_direction = [up(), up_right(), right(), down_right(), down()]
    elif i==last_row:
        valid_direction = [left(), up_left(), up(), up_right(), right()]
    elif j==last_column:
        valid_direction = [down(), down_left(), left(), up_left(), up()]
    else:
        valid_direction = [up(), up_right(), right(), down_right(), down(), down_left(), left(), up_left()]

    for direction in valid_direction:
        if direction == '@':
            count += 1
    
    return count


def main():
    
    input: list = pandas.read_csv('day_4_input.csv')['rows'].to_list()
    # input: list = pandas.read_csv('day_4_input_test.csv')['rows'].to_list()
    grid: list = [list(row) for row in input]

    first_row:int = 0
    first_column: int = 0
    last_row: int = len(grid) - 1
    last_column: int = len(grid[0]) - 1

    accessible_rolls: int = 0

    for i, row in enumerate(grid):
        for j, column in enumerate(row):

            if grid[i][j] == '@':

                num_rolls: int = count_rolls(
                    grid, i, j,
                    first_row, last_row,
                    first_column, last_column
                )

                if num_rolls < 4:
                    accessible_rolls += 1

    print(f'accessible rolls: {accessible_rolls}')

if __name__ == "__main__":
    main()