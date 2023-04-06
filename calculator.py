"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
input_file = open('input.txt').readlines()
output_file = open('output.txt', 'a')

for line in input_file:
    user_input = line.split()  # 여기서는 왜 split(' ')를 안해도 되는지 물어보기!!

    # if user_input[0] == 'q':
    #     break

    operator = user_input[0]
    num1 = user_input[1]
    if len(user_input) < 3:
        num2 = '0'
    else:
        num2 = user_input[2]

    # print(f'{num1}: {num1.isdigit()}, {num2}: {num2.isdigit()}')

    if not num1.isdigit() or not num2.isdigit():
        output_file.write('Those aren\'t numbers!!\n')
        continue

    result = None

    if operator == '+':
        result = format(add(float(num1), float(num2)), '.2f')
    elif operator == '-':
        result = format(subtract(float(num1), float(num2)), '.2f')
    elif operator == '*':
        result = format(multiply(float(num1), float(num2)), '.2f')
    elif operator == '/':
        result = format(divide(float(num1), float(num2)), '.2f')
    elif operator == 'square':
        result = format(square(float(num1)), '.2f')
    elif operator == 'cube':
        result = format(cube(float(num1)), '.2f')
    elif operator == 'pow':
        result = format(power(float(num1), float(num2)), '.2f')
    elif operator == 'mod':
        result = format(mod(float(num1), float(num2)), '.2f')
    else:
        print('Syntax error!!')

    output_file.write(str(result) + '\n')


output_file.close()
