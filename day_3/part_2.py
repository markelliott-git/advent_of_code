import pandas

def find_num(bank: list, battery: int):

    if battery == 1:

        truncated_bank = bank

    else: 
        truncated_bank = bank[:-battery+1]
    
    for digit in range(9, -1, -1):
        for idx, num in enumerate(truncated_bank):
            if digit == int(num):
                truncated_bank = bank[idx+1:]

                return num, truncated_bank

def main():

    num_batteries = 12
    total_joltage = 0
    input: list = pandas.read_csv('day_3_input.csv')['banks'].to_list()

    for bank in input:
        bank_list: list = list(bank)

        batteries = []
        truncated_bank = bank_list
        for battery in range(num_batteries, 0, -1):

            num, truncated_bank = find_num(truncated_bank, battery) 

            batteries.append(num)

        joltage: int = int(''.join(batteries)) 

        total_joltage += joltage

    
    print(f'Total Joltage: {total_joltage}')


if __name__ == "__main__":
    main()
