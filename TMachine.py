'''
___________                 .__                                      .__    .__                  _____.__.__          
\__    _______  __ _________|__| ____   ____     _____ _____    ____ |  |__ |__| ____   ____   _/ ____|__|  |   ____  
  |    | /  _ \|  |  \_  __ |  |/    \ / ___\   /     \\__  \ _/ ___\|  |  \|  |/    \_/ __ \  \   __\|  |  | _/ __ \ 
  |    |(  <_> |  |  /|  | \|  |   |  / /_/  > |  Y Y  \/ __ \\  \___|   Y  |  |   |  \  ___/   |  |  |  |  |_\  ___/ 
  |____| \____/|____/ |__|  |__|___|  \___  /  |__|_|  (____  /\___  |___|  |__|___|  /\___  >  |__|  |__|____/\___  >
                                    \/_____/         \/     \/     \/     \/        \/     \/                      \/ 

                                    
'''
import copy
from TTape import Tape, bcolors
import timeit
        
class TuringMachine(object):
    
    def __init__(self, 
                 blank_symbol = " ",
                 initial_state = "",
                 final_states = None,
                 transition_function = None , accept_states = None):
        self.__init = initial_state
        self.__curr = 0
        self.__blank_symbol = blank_symbol
        self.__tape = None
        self.__head_position = 0
        self.__current_state = initial_state
        self.__immediate_description = None
        self.__accept_states = accept_states
        if transition_function == None:
            self.__transition_function = {}
        else:
            self.__transition_function = transition_function
        if final_states == None:
            self.__final_states = set()
        else:
            self.__final_states = set(final_states)
           
    def evaluate_strings(self,string:str):
        self.__tape = Tape(string,self.__blank_symbol)

        print("=================================")
        print("Input on Tape:\n" + self.get_tape())
        print("---------------------------------")
        while not self.final():
            self.step()
        print("---------------------------------")
        if (self.__accept_states):
            if self.__current_state in self.__accept_states:
                print("String accepted")
            else:
                print("String not accepted")
        else:
            print("Machine has not accept nor reject")
        print("---------------------------------")
        print("Result of the Turing machine calculation:")
        tape = self.get_tape()
        tape = tape.replace(self.__blank_symbol, '')
        print(tape)
        print("---------------------------------")
        return tape
    
    def evaluate_strings_timed(self,string:str):
        self.__tape = Tape(string,self.__blank_symbol)
        start = timeit.default_timer()
        while not self.final():
            self.step(ignore_prints=True)
        return timeit.default_timer() - start

    def get_tape(self): 
        return str(self.__tape)
    
    
    def step(self):
        char_under_head = self.__tape[self.__head_position]
        self.generate_immediate_description(True)
        x = (self.__current_state, char_under_head)
        if x in self.__transition_function:
            y = self.__transition_function[x]
            self.__tape[self.__head_position] = y[1]
            if y[2] == "R":
                self.__head_position += 1
            elif y[2] == "L":
                self.__head_position -= 1
            self.__current_state = y[0]        
            self.generate_immediate_description(False)

    def final(self):
        if self.__current_state in self.__final_states:
            return True
        else:
            return False
        
    def generate_immediate_description(self, first:bool):
        if (first):
            self.__immediate_description = copy.deepcopy(self.__tape)
            self.__immediate_description[self.__head_position]= bcolors.FAIL +  self.__current_state + bcolors.ENDC +self.__immediate_description[self.__head_position]
        else:
            immediate_description = copy.deepcopy(self.__tape)
            immediate_description[self.__head_position]= bcolors.FAIL +  self.__current_state + bcolors.ENDC+self.__immediate_description[self.__head_position]
            print(str(self.__immediate_description)+" ├─ "+str(immediate_description))