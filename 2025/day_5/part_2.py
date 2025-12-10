import pandas

def split_range(id_range: str):
    start_range, end_range = id_range.split('-')
    start_range = int(start_range)
    end_range = int(end_range)

    return start_range, end_range

def check_and_merge(
    start_range, end_range,
    new_start_range, 
    new_end_range,
    ):

    range_merged_flag: bool = False
    merged_range: str = f'{new_start_range}-{new_end_range}'

    if start_range >= new_start_range and start_range <= new_end_range:
        if end_range <= new_end_range:
            merged_range = f'{new_start_range}-{new_end_range}'
        elif end_range > new_end_range:
            merged_range = f'{new_start_range}-{end_range}'

        range_merged_flag = True

    elif end_range <= new_end_range and end_range >= new_start_range:
        if start_range <= new_start_range:
            merged_range =f'{start_range}-{new_end_range}'
        elif start_range > new_start_range:
            merged_range = f'{new_start_range}-{new_end_range}'

        range_merged_flag = True
    
    return merged_range, range_merged_flag

def main():

    fresh_count: int = 0
    # ranges: list = pandas.read_csv('day_5_input_ranges.csv')['ranges'].to_list()
    ranges: list = pandas.read_csv('day_5_input_ranges_test.csv')['ranges'].to_list()

    new_ranges: list = [ranges[0]]

    for id_range in ranges[1:]:

        start_range, end_range = split_range(id_range)
 
        range_merged_flag: bool = False
        for i, new_range in enumerate(new_ranges):
            new_start_range, new_end_range = split_range(new_range)

            merged_range, range_merged_flag = check_and_merge(
                start_range, end_range,
                new_start_range, new_end_range)
            
            if range_merged_flag:
                new_ranges[i] = merged_range

                # while range_merged_flag:
                #     new_ranges[i] = merged_range
            

            
            print(new_ranges)
        
        if range_merged_flag == False:
            new_ranges.append(id_range)

    id_count: int = 0
    for final_range in new_ranges:
        final_start_range, final_end_range = split_range(final_range)

        id_count += final_end_range - final_start_range + 1
    
    print(f'Total IDs: {id_count}')
        
if __name__ == "__main__":
    main()