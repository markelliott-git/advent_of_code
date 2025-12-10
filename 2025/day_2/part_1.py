import math
import pandas

def check_id(id: int):
    id_string = str(id)
    id_length = len(id_string)

    if id_length % 2 == 0:
        first_half = id_string[0:id_length//2]
        second_half = id_string[id_length//2:]

        if first_half == second_half:

            return id
        else:
            return None


def main():
    invalid_ids = []
    invalid_id_sum = 0
    input = pandas.read_csv('day_2_input.csv').columns.to_list()
    # input = pandas.read_csv('day_2_input_test.csv').columns.to_list()

    for id_range in input:
        
        id_start, id_end = id_range.split('-')
        id_start = int(id_start)
        id_end = int(id_end)

        id_current = id_start

        while id_current <= id_end:

            checked_id = check_id(id_current)    
            if checked_id:
                invalid_ids.append(checked_id)
                invalid_id_sum += checked_id

            id_current += 1

    print('\n')
    print(f'invalid ids: {invalid_ids}')
    print('\n')
    print(f'sum of invaild ids: {invalid_id_sum}')
    print(f'sum of invaild ids: {sum(invalid_ids)}')


if __name__ == "__main__":
    main()
