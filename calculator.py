import os, math, random
from memory import *
from calculations import *

g_memory_name = ''
g_memory_value = []

class commands():
    def __init__(self):
        self.cmds_keys = {}

        self.cmds_keys['h'] = 'h'
        self.cmds_keys['q'] = 'q'
        self.cmds_keys['b'] = 'b'
        self.cmds_keys['par'] = 'par'
        self.cmds_keys['trig'] = 'trig'
        self.cmds_keys['rand'] = 'rand'
        self.cmds_keys['mem'] = 'mem'
        self.cmds_keys['del'] = 'del'
        self.cmds_keys['calc'] = 'calc'
        self.cmds_keys['rmap'] = 'rmap'

    def remap(self, cmd_to_remap, cmd_remapped):
        key_counter = 0

        for value in self.cmds_keys.values():
            if cmd_remapped == value:
                key_counter = key_counter+1
        if key_counter == 0:
            for name,value in self.cmds_keys.items():
                if value == cmd_to_remap:
                    self.cmds_keys[name] = cmd_remapped
                    print(cmd_to_remap + " successfully remapped to " + 
                          self.cmds_keys[name] + "\n")
        elif key_counter > 0:   
            print('Command already in use.\n')

def exit_program():
    os._exit(1)

def throw_error(error_code):
    if error_code == 0:
        print("\nInvalid input.\n")
    elif error_code == 1:
        print("\nInvalid operation.\n")
    else:
        print("\nUnknown error.\n")

def boot():
    boot_cmds = commands()
    global g_memory_value
    global g_memory_name
    return boot_cmds

def help(main_cmds):
    help_lines = [main_cmds.cmds_keys['q'] + " to quit", 
                  main_cmds.cmds_keys['b'] + " to access previous menu",
                  main_cmds.cmds_keys['h'] + " to show help menu", 
                  main_cmds.cmds_keys['par'] + " to calculate parity", 
                  main_cmds.cmds_keys['trig'] + " to calculate cosine and"
                 "sine ", 
                  main_cmds.cmds_keys['rand'] + " to generate random"
                 "numbers", 
                  main_cmds.cmds_keys['mem'] + " to visualize memorized"
                 "variables", 
                  main_cmds.cmds_keys['del'] + " to delete memorized"
                 "variables", 
                  main_cmds.cmds_keys['calc'] + " to operate with memorized"
                 "variables", 
                  main_cmds.cmds_keys['rmap'] + " to remap a command"]
    
    help_print_output = "\n-------------- COMMANDS --------------\n\n"

    for help_line in help_lines:
        help_print_output += "Type " + help_line + "\n"

    print(help_print_output)

def main(boot_cmds):
    global g_memory_name
    global g_memory_value

    main_cmds = boot_cmds
    memory_cells = []

    print("Type 'h' for help and a list of all available commands.")
    while True:
        menu_level_pointer = ">>:"

        input_str = input_handler(menu_level_pointer)

        if input_str == main_cmds.cmds_keys['q']:
            exit_program()
        elif input_str == main_cmds.cmds_keys['b']:
            print("Already at main menu.\n")
        elif input_str == main_cmds.cmds_keys['h']:
            help(main_cmds)
        elif input_str == main_cmds.cmds_keys['par']:
            calc_parity(main_cmds)
        elif input_str == main_cmds.cmds_keys['trig']:
            calc_trig(main_cmds)
        elif input_str == main_cmds.cmds_keys['rand']:
            calc_rand(main_cmds)
        elif input_str == main_cmds.cmds_keys['rmap']:
            calc_remap(main_cmds)
        elif input_str == main_cmds.cmds_keys['mem']:
            print('\nSaved Variables:')
            for i in range(len(memory_cells)):
                for name,value in memory_cells[i].object.items():
                    print(name + '=' + str(value))
            print('\n')
        elif input_str == main_cmds.cmds_keys['del']:
            memory_delete(memory_cells)
        elif input_str == main_cmds.cmds_keys['calc']:
            calculate(main_cmds, memory_cells)
        else:
            memory_cells.append(memory_cell(input_str))
            memory_cleanup(memory_cells)

main(boot())
