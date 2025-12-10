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
    merged_range = f'{new_start_range}-{new_end_range}'

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
    else:
        merged_range = None
    
    return merged_range, range_merged_flag


def main():

    ranges: list = pandas.read_csv('day_5_input_ranges.csv')['ranges'].to_list()
    # ranges: list = pandas.read_csv('day_5_input_ranges_test.csv')['ranges'].to_list()

    merged: bool = True
    while merged:
        for id_range in ranges:
            # print('\n', id_range)
            # print('--------------')

            start_range_1, end_range_1 = split_range(id_range)
            other_ranges = [itm for itm in ranges if itm != id_range] 

            for other_id_range in other_ranges:
                # print(other_id_range)
                # print(other_ranges)

                start_range_2, end_range_2 = split_range(other_id_range)
                
                merged_range, merged = check_and_merge(
                    start_range_1,
                    end_range_1,
                    start_range_2,
                    end_range_2
                )

                if merged:
                    ranges.remove(id_range)
                    ranges.remove(other_id_range)
                    ranges.append(merged_range)
                    # print(f'merged {id_range} and {other_id_range}')

                    break
        
            if merged:
                break

        # stop checking if there is only 1 range
        if len(ranges) == 1:
            break

    
    print(f'\nfinal ranges: {ranges}')
    # count the Ids and get the solution
    id_count: int = 0
    for final_range in ranges:
        final_start_range, final_end_range = split_range(final_range)

        id_count += final_end_range - final_start_range + 1
    
    print(f'\nTotal IDs: {id_count}')
        

if __name__ == "__main__":
    main()
    

    # 394346020079876 - wrong
    # 378077676215858 - wrong