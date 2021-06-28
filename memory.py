import os, math

class memory_cell():
    def __init__(self, input_str):
        global g_memory_name
        global g_memory_value
        try: 
            g_memory_value
        except:
            g_memory_value = ''
            g_memory_name = ''
        self.object = {}
        self.values_container = []
        self.values_container_row = []
        input_string_handler(input_str) #global variables setter
        self.dimension = calc_dimesion(input_str)
        if self.dimension == 0:
            self.object[g_memory_name] = g_memory_value
        elif self.dimension == 1:
            for input_value in g_memory_value:
                self.values_container.append(input_value)
            self.object[g_memory_name] = self.values_container
        elif self.dimension**2 == len(g_memory_value):
            i = 0
            for input_value in g_memory_value:
                self.values_container_row.append(input_value)
                if i == (self.dimension-1):
                    self.values_container.append(self.values_container_row)
                    self.values_container_row = []
                    i = -1
                i = i + 1
            self.object[g_memory_name] = self.values_container
        else:
            print("\nInvalid input.\n")
            
# tensor index dimension 0 for scalar, 1 for contravariant vector, 
# n>1 for any (1,1) tensor (nxn matrix)
def calc_dimesion(input_string): 
    global g_memory_value
    if type(g_memory_value) is float or type(g_memory_value) is bool:
        dimension = 0
    else:
        if input_string.count(';') == 0:
            dimension = 1
        elif math.sqrt(len(g_memory_value)).is_integer() and (
        input_string.count(';') > 0):
            dimension = math.sqrt(len(g_memory_value))
        else:
            dimension = 0
    return dimension
def memory_cleanup(memory_cells):
    global g_memory_value
    if g_memory_value == False:
        memory_cells.pop(-1)
        g_memory_value = []
    for i in range(len(memory_cells)-1):
        if memory_cells[-1].object.keys() == memory_cells[i].object.keys():
            memory_cells.pop(i)
            break
    for i in range(len(memory_cells)):
        if str(memory_cells[i].object.values()) == 'dict_values([[]])':
            memory_cells.pop(i)

def memory_delete(memory_cells):
    if len(memory_cells) != 0:
        print('Saved Variables:')
        for i in range(len(memory_cells)):
            for name,value in memory_cells[i].object.items():
                print(name + '=' + str(value))
        input_str = input('\n>> type a variable to delete: ')
        loop_exit_token = False
        for i in range(len(memory_cells)):
            if loop_exit_token == True:
                break
            for name in memory_cells[i].object.keys():
                if name == input_str:
                    input_str = input('>> are you sure you want do delete ' +
                                     input_str + '? (y/n): ')
                    if input_str == 'y':
                        memory_cells.pop(i)
                        i = len(memory_cells) + 1
                        loop_exit_token = True
                        #loop_exit_token = True
                    elif input_str == 'n':
                        break
                    else:
                        print("\nInvalid input.\n")
                        break
    else:
        print('There are no saved variables')


def input_string_handler(input_string):
    global g_memory_name
    global g_memory_value
    input_string.replace(' ', '')
    if input_string.count('=') == 1:
        equal_sign_pos = input_string.find('=')      
        input_string_name = input_string[:equal_sign_pos]
        input_string_values = input_string[equal_sign_pos+1:]       
        g_memory_name = input_string_name
        if input_string_values != '' and (
            input_string_values.count('(') == 1) and (
            input_string_values.count(')') == 1) and (
            input_string_values.find('(') < input_string_values.find(')')) or(
            input_string_values.count('[') == 1) and (
            input_string_values.count(']') == 1) and (
            input_string_values.find('[') < input_string_values.find(']')):
            input_string_values = input_string_values.replace('(','')
            input_string_values = input_string_values.replace(')','')
            input_string_values = input_string_values.replace('[','')
            input_string_values = input_string_values.replace(']','')
            if input_string_values.count(';') == 0: #vector handler
                input_str_val_rows_split = input_string_values.split(',')
                input_str_val_split = []
                for i in range(len(input_str_val_rows_split)):
                    try:
                        input_str_val_split.append(
                            float(input_str_val_rows_split[i]))
                    except:
                        print("\nInvalid input.\n")
                        break
                g_memory_value = input_str_val_split
            #matrix handler
            else: 
                input_str_val_rows = input_string_values.split(';')
                input_str_val_rows_split = []
                input_str_val_split = []
                for i in range(len(input_str_val_rows)):
                    input_str_val_rows_split = input_str_val_rows[i].split(
                    ',')
                    for j in range(len(input_str_val_rows_split)):
                        try:
                            input_str_val_split.append(float(
                                input_str_val_rows_split[j]))
                        except:
                            print("\nInvalid input.\n")
                            break
                if math.sqrt(len(input_str_val_split)).is_integer():
                    g_memory_value = input_str_val_split
                else:
                    print("\nInvalid input.\n")
                    g_memory_value = False
        #scalar handler
        else: 
            try:
                input_string_values = float(input_string_values)
                g_memory_value = input_string_values
            except:
                print("\nInvalid input.\n")
                g_memory_value = ''
    else:
        print("\nInvalid input.\n")
