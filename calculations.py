import os, math, random
from copy import deepcopy

def exit_program():
    exit(0)

def throw_error(x):
    print('Input error')
    exit(x)

def input_handler(menu_level_pointer):
    input_arg = input(menu_level_pointer)
    return str(input_arg)

def calc_parity(main_cmds):
    print("\nType q to quit, b to return to main menu\nType a number to"
         "calculate parity")
    while True:      
        menu_level_pointer = ">> " + main_cmds.cmds_keys['par'] + ":"

        input_str = input_handler(menu_level_pointer)

        if input_str == main_cmds.cmds_keys['b']:
            break
        elif input_str == main_cmds.cmds_keys['q']:
            exit_program()
        else:
            try:
                x = int(float(input_str))

                if x%2 == 0:
                    print("even")
                else:
                    print("odd")
            except: 
                throw_error(0)

def calc_trig(main_cmds):
    print("\nType q to quit, b to return to main menu\nType sin or cos to"
         "access sine and cosine functions")
    while True:   
        menu_level_pointer = ">> " + main_cmds.cmds_keys['trig'] + ":"
        sin_pointer = ">> sin:"
        cos_pointer = ">> cos:"

        input_str = input_handler(menu_level_pointer)

        if input_str == main_cmds.cmds_keys['b']:
            break
        elif input_str == main_cmds.cmds_keys['q']:
            exit_program()
        elif input_str == "sin":
            print("Insert angle in radiants")
            input_str = input_handler(sin_pointer)
            try:
                x = math.sin(float(input_str))
                print(x)
            except:
                throw_error(0)
        elif input_str == "cos":
            print("Insert angle in radiants")
            input_str = input_handler(cos_pointer)
            try:
                x = math.cos(float(input_str))
                print(x)
            except:
                throw_error(0)

def calc_rand(main_cmds):
    print("\nType q to quit, b to return to main menu\nType in a scale X"
         "for the random number N between 0 and 1. The result will be X*N. ")
    while True:
        menu_level_pointer = ">> " + main_cmds.cmds_keys['rand'] + ":"

        input_str = input_handler(menu_level_pointer)
        # input = b, loop quit condition
        if input_str == main_cmds.cmds_keys['b']:  
            break
        # input = q, abort condition
        elif input_str == main_cmds.cmds_keys['q']:   
            exit_program()
        else:
            try:
                x = random.random()*float(input_str)
                print(x)
            except:
                throw_error(0)

def calc_remap(main_cmds):
    print("\nType q to quit, b to return to main menu\nType the command"
         "you whish to remap, type h for a list of all available"
        "commands\n(q,b,h not remappable)")
    while True:
        menu_level_pointer = ">> old key to remap:"

        input_str = input_handler(menu_level_pointer)

        if input_str == main_cmds.cmds_keys['b']:
            break
        elif input_str == main_cmds.cmds_keys['q']:
            exit_program()
        elif input_str == main_cmds.cmds_keys['h']:
            help(main_cmds)
        elif input_str in main_cmds.cmds_keys.values():
            old_input_str = input_str
            menu_level_pointer = ">> new key to remap:"
            input_str = input_handler(menu_level_pointer)
            
            main_cmds.remap(old_input_str, input_str)
            break
        elif input_str not in main_cmds.cmds_keys.values():
            print('Unexisting command.\n')
            break

def calculate(main_cmds, memory_cells):
    print("\nType q to quit, b to return to main menu, " + 
          main_cmds.cmds_keys['mem'] + " to visualize saved variables\n")

    while True:
        menu_level_pointer = ">> calc:"

        input_str = input_handler(menu_level_pointer)

        if input_str == main_cmds.cmds_keys['b']:
            break
        elif input_str == main_cmds.cmds_keys['q']:
            exit_program()
        elif input_str == main_cmds.cmds_keys['h']:
            help(main_cmds)
        elif input_str in main_cmds.cmds_keys['mem']:
            print('\nSaved Variables:')
            for i in range(len(memory_cells)):
                for name,value in memory_cells[i].object.items():
                    print(name + '=' + str(value))
            print('\n')
            break
        else:
            input_str.replace(' ', '')

            input_variables_counter = 0
            input_operators_counter = 0
            allowed_operators = ['+', '-', '*', '/']
            var_to_calc = [0,1]
            variables_to_calc_name = []

            for allowed_operator in allowed_operators:
                if input_str.count(allowed_operator) == 1:
                    input_operators_counter = input_operators_counter + 1
                    operator_sign = allowed_operator

            variables_to_calc_name = input_str.split(operator_sign)

            for i in range(len(memory_cells)): # operand assignment
                for name, value in memory_cells[i].object.items():
                    if variables_to_calc_name[0] == name:
                        input_variables_counter = input_variables_counter + 1
                        var_to_calc[0] = value
                    elif variables_to_calc_name[1] == name:
                        input_variables_counter = input_variables_counter + 1
                        var_to_calc[1] = value

            if input_str.find(variables_to_calc_name[1]) < input_str.find(
                variables_to_calc_name[0]): # operand reordering
                var_to_calc[1]
                var_to_calc[0] = var_to_calc[0]
                var_to_calc[1]

            if input_variables_counter == 2 and input_operators_counter == 1:
                # sum
                if operator_sign == '+': 
                    if type(var_to_calc[0]) is float and (
                    type(var_to_calc[1]) is float): # scalars summation
                        result = var_to_calc[0] + var_to_calc[1]
                        print(str(var_to_calc[0]) + '+' + 
                              str(var_to_calc[1]) + '=' + str(result))
                    # scalar-vector/matrix summation
                    elif type(var_to_calc[0]) is float and (
                    type(var_to_calc[1]) is not float) or (
                    type(var_to_calc[0]) is not float) and (
                    type(var_to_calc[1]) is float): 
                        print('Cannot sum vectors/matrices and scalars')
                    # vector-vector matrix-matrix summation
                    elif type(var_to_calc[0]) is not float and (
                        type(var_to_calc[1]) is not float): 
                        if len(var_to_calc[0]) == len(
                            var_to_calc[1]):
                            calc_result = []
                            calc_result_row = []

                            for i in range(len(var_to_calc[0])):
                                if type(var_to_calc[0][i]) is float and (
                                    type(var_to_calc[1][i]) is float):
                                    calc_result.append(var_to_calc[0][i] +
                                                       var_to_calc[1][i])
                                elif type(var_to_calc[0][i]) is not float and(
                                   type(var_to_calc[1][i]) is not float):
                                    for j in range(len(var_to_calc[1][i])):
                                        calc_result_row.append(
                                            var_to_calc[1][i][j] + 
                                            var_to_calc[0][i][j])
                                        calc_result.append(calc_result_row)
                                        calc_result_row = []

                            print(str(var_to_calc[0]) + ' + ' + 
                                  str(var_to_calc[1]) + ' = ' + 
                                  str(calc_result))
                        else:
                            print('Variables are not of the same dimension')
                # subtraction
                elif operator_sign == '-': 
                    # scalars subtraction
                    if type(var_to_calc[0]) is float and (
                        type(var_to_calc[1]) is float): 
                        result = var_to_calc[0] - var_to_calc[1]
                        print(str(var_to_calc[0]) + '-' + 
                              str(var_to_calc[1]) + '=' + str(result))
                    # scalar-vector/matrix subtraction
                    elif type(var_to_calc[0]) is float and (
                        type(var_to_calc[1]) is not float) or (
                            type(var_to_calc[0]) is not float) and (
                                type(var_to_calc[1]) is float): 
                        print('Cannot subtract vectors/matrices and scalars')
                # multiplication
                elif operator_sign == '*':
                    # scalars multiplication
                    if type(var_to_calc[0]) is float and (
                        type(var_to_calc[1]) is float): 
                        result = var_to_calc[0] * var_to_calc[1]
                        print(str(var_to_calc[0]) + '*' + 
                              str(var_to_calc[1]) + '=' + str(result))
                    # scalar-vector/matrix multiplication
                    elif type(var_to_calc[0]) is float and (
                        type(var_to_calc[1]) is not float): 
                        calc_result = []
                        calc_result_row = []

                        for i in range(len(var_to_calc[1])):
                            # scalar-vector multiplication (scalar product)
                            if type(var_to_calc[1][i]) is float: 
                                calc_result.append(var_to_calc[1][i] * 
                                                   var_to_calc[0])
                            #scalar-matrix multiplication (scalar product)
                            else: 
                                for j in range(len(var_to_calc[1][i])):
                                    calc_result_row.append(
                                        var_to_calc[1][i][j] * var_to_calc[0])
                                calc_result.append(calc_result_row)
                                calc_result_row = []
                                
                        print(str(var_to_calc[0]) + ' * ' + 
                              str(var_to_calc[1]) + ' = ' + str(calc_result))
                    # vector/matrix-scalar multiplication
                    elif type(var_to_calc[0]) is not float and (
                        type(var_to_calc[1]) is float):  
                        calc_result = []
                        calc_result_row = []

                        for i in range(len(var_to_calc[0])):
                            # vector-scalar multiplication
                            if type(var_to_calc[0][i]) is float: 
                                calc_result.append(var_to_calc[0][i] * 
                                                   var_to_calc[1])
                            # matrix-scalar multiplication
                            else: 
                                for j in range(len(var_to_calc[0][i])):
                                    calc_result_row.append(
                                        var_to_calc[0][i][j] * var_to_calc[1])
                                calc_result.append(calc_result_row)
                                calc_result_row = []
                        print(str(var_to_calc[0]) + ' * ' + 
                              str(var_to_calc[1]) + ' = ' + str(calc_result))
                    #vector/matrix-vector/matrix multiplication  
                    elif type(var_to_calc[0]) is not float and (
                        type(var_to_calc[1]) is not float): 
                        calc_result = []
                        calc_result_row = []
                        calc_coloumn = []

                        if len(var_to_calc[0]) != len(var_to_calc[1]):
                            print('Variables are not of the same dimension')
                        else:
                            calc_temp_sum = 0
                            # vector-vector multiplication (scalar product)
                            for i in range(len(var_to_calc[0])):      
                                if type(var_to_calc[0][i]) is float and (
                                    type(var_to_calc[1][i]) is float): 
                                    calc_temp_sum = calc_temp_sum +(
                                    var_to_calc[0][i] * var_to_calc[1][i])
                                    if i == (len(var_to_calc[0])-1):
                                        calc_result.append(calc_temp_sum)
                                # vector-matrix multiplication
                                elif type(var_to_calc[0][i]) is float and (
                                    type(var_to_calc[1][i]) is not float): 
                                    for j in range(len(var_to_calc[0])):
                                        calc_coloumn.append(
                                            var_to_calc[1][j][i])
                                    calc_temp_sum = 0
                                    for j in range(len(var_to_calc[0])):
                                        calc_temp_sum = calc_temp_sum +( 
                                        var_to_calc[0][j]*calc_coloumn[j])
                                    calc_result_row.append(calc_temp_sum)

                                    calc_result.append(calc_result_row[0])
                                    calc_result_row = []
                                    calc_coloumn = []
                                # matrix-vector multiplication
                                elif type(var_to_calc[0][i]) is not float and(
                                    type(var_to_calc[1][i]) is float): 
                                    for j in range(len(var_to_calc[1])):
                                        calc_coloumn.append(
                                            var_to_calc[0][j][i])
                                    calc_temp_sum = 0
                                    for j in range(len(var_to_calc[1])):
                                        calc_temp_sum = calc_temp_sum + (
                                            var_to_calc[1][j]*calc_coloumn[j])
                                    calc_result_row.append(calc_temp_sum)

                                    calc_result.append(calc_result_row[0])
                                    calc_result_row = []
                                    calc_coloumn = []
                                # matrix-matrix multiplication
                                elif type(var_to_calc[0][i]) is not float and( 
                                    type(var_to_calc[1][i]) is not float):  
                                    calc_result = deepcopy(var_to_calc[0])
                                    for j in range(len(calc_result[i])):
                                        for k in range(len(calc_result[i])):
                                            calc_result[j][k] = 0.0

                                    for l in range(len(var_to_calc[0])):
                                        for j in range(len(var_to_calc[0])):
                                            for k in range(len(
                                                var_to_calc[0])):
                                                calc_result[l][j] += (
                                                    var_to_calc[0][l][k]*(
                                                        var_to_calc[1][k][j]))
                                    break #(not iterable on main loop)
                            print(str(var_to_calc[0]) + ' * ' + 
                                  str(var_to_calc[1]) + ' = ' + 
                                  str(calc_result))
                # division
                elif operator_sign == '/': 
                    # scalars division
                    if type(var_to_calc[0]) is float and (
                        type(var_to_calc[1]) is float): 
                        if var_to_calc[1] != 0:
                            result = var_to_calc[0] / var_to_calc[1]
                        else:
                            print('Error cannot divide by 0')
                        print(str(var_to_calc[0]) + '/' + 
                              str(var_to_calc[1]) + '=' + str(result))
                    else:
                        print('Unable to divide non scalar variables')
            else:
                print('Wrong syntax.\n')
