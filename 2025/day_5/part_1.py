import pandas


def main():

    fresh_count: int = 0
    ranges: list = pandas.read_csv('day_5_input_ranges.csv')['ranges'].to_list()
    ids: list = pandas.read_csv('day_5_input_ids.csv')['ids'].to_list()

    for id in ids:

        for range in ranges:

            start_range, end_range = range.split('-')
            start_range = int(start_range)
            end_range = int(end_range)

            if int(id) >= start_range and int(id) <= end_range:
                fresh_count += 1
                break

    print(f'Fresh Items: {fresh_count}')            

if __name__ == "__main__":
    main()