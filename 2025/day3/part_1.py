import pandas

def find_first_num(bank_list: list):
    truncated_bank = bank_list[:-1] 

    for digit in range(9, -1, -1):
        for idx, num in enumerate(truncated_bank):
            if digit == int(num):

                return idx, num

def find_second_num(bank_list: list, first_idx):
    truncated_bank = bank_list[first_idx+1:]

    for digit in range(9, -1, -1):
        for idx, num in enumerate(truncated_bank):
            if digit == int(num):

                return idx, num

def main():

    total_joltage = 0
    input: list = pandas.read_csv('day_3_input.csv')['banks'].to_list()

    for bank in input:
        bank_list: list = list(bank)
        bank_length: int = len(bank_list)

        first_idx, first_num = find_first_num(bank_list)
        second_idx, second_num = find_second_num(bank_list, first_idx)


        joltage: int = int(first_num + second_num) 

        total_joltage += joltage

    
    print(f'Total Joltage: {total_joltage}')


if __name__ == "__main__":
    main()
