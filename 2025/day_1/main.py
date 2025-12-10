import pandas


def tick(position, direction):
    if direction == 'L':
        if position == 0:
            position = 99
        else:
            position -= 1
    elif direction =='R':
        if position == 99:
            position = 0
        else:
            position += 1

    return position

def main():
    starting_position = 50
    password1 = 0
    password2 = 0

    input = pandas.read_csv('day_1_input.csv')['instruction'].to_list()

    position = starting_position

    for instruction in input:
        direction = instruction[0]
        rotations = int(instruction[1:])

        for _ in range(rotations):
            position = tick(position, direction)

            if position == 0:
                password2 += 1

        if position == 0:
            password1 += 1
    
    print(f'Part 1 password: {password1}')
    print(f'Part 2 password: {password2}')
    
if __name__ == "__main__":
    main()
