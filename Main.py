''' 
MAIN File
'''
from FileReader import *
import time
# create_turing_machine_graph("./fibonacci_machine.yaml")
t = createTouringFromFile("./fibonacci_machine.yaml")

while True:
    numer = input("Ingrese el numero de fibonnacci a evaluar , para salir ingrese q \n")
    if numer == 'q':
        break
    start = time.time()
    res = t.evaluate_strings("".join(['|' for _ in range(int(numer))]))
    end = time.time()
    print(f"result in decimals: {res.count('|')}")
    print(f"result in seconds: {end - start}")
