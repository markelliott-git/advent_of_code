import math
import pandas

def group_numbers(id_string: str, group_size: int):
    num_of_groups: int = math.floor(len(id_string) / group_size)

    grouped_id: list = []
    if group_size == 1:
        grouped_id = list(id_string)
    else:
        tmp_id_string = id_string
        for _ in range(num_of_groups):
            id_chunk = tmp_id_string[0:group_size]
            tmp_id_string = tmp_id_string[group_size:]

            grouped_id.append(id_chunk)

    return grouped_id

def check_id(id: int):
    id_string = str(id)
    id_length = len(id_string)

    if id_length == 1:
        return None

    elif id_length == 2:
        valid_group_sizes = [1]

    else:
        valid_group_sizes = []
        for length in range(1, id_length):
            if id_length % length == 0:
                valid_group_sizes.append(length)
        
    for group_size in valid_group_sizes:

        grouped_id = group_numbers(id_string, group_size)

        if len(set(grouped_id)) == 1:
   
            return id

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
