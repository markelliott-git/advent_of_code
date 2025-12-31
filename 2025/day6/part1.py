
INPUT_FILE: str = '../../advent_of_code_inputs/2025/day6/day_6_input.txt'

def main():
    with open(INPUT_FILE, 'r') as f:
        input = f.readlines()
    
    # remove white space and new line characters from operand lines
    operands: list = input[:-1]
    operands = [line.replace('\n', '') for line in operands]
    operands = [line.split(' ') for line in operands]
    operands = [list(filter(lambda x: x != '', line)) for line in operands]
    operands = [[int(num) for num in line] for line in operands]

    # remove white space and new line characters from operator line
    operators: list = [input[-1]][0]
    operators = operators.split(' ')
    operators = list(filter(lambda x: x != '', operators))


    expressions = zip(
        operands[0], operands[1],
        operands[2], operands[3],
        operators)
    
    total: int = 0
    for op1, op2, op3, op4, operator in expressions: 
        if operator == '*':
            results = op1 * op2 * op3 * op4
        elif operator == '+':
            results = op1 + op2 + op3 + op4
        
        total += results  
    

    print(total)

if __name__ == "__main__":
    main()