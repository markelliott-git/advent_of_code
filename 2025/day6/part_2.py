

def main():
    with open('day_6_input.txt', 'r') as f:
        input = f.readlines()
    
    
    # format operands
    operands: list = input[:-1]

    split_operands: list = []
    for line in operands:
        char_list: list = [char for char in line if char != '\n']
        char_list.reverse()
        split_operands.append(char_list)

    # format operators
    operators: str = input[-1]
    split_operators = [char for char in operators]
    split_operators.reverse()

    # combine and compute
    operand_buffer: list = []
    total: int = 0
    for nums in zip(*split_operands, split_operators):
        nums_bool: list = [True if itm == ' ' else False for itm in nums]
        
        if all(nums_bool):
            operand_buffer = []
            continue
        else:
            operand = int(''.join(nums[:-1]))
            operand_buffer.append(operand)
        
        if nums[-1] != ' ':
            operator = nums[-1]
            
            result: int = operand_buffer[0]
            for op in operand_buffer[1:]:
                if operator == '*':
                    result *= op
                elif operator == '+':
                    result += op

            total += result


    print(total) 
        

if __name__ == "__main__":
    main()