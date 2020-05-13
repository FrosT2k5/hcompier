import os
import sys

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def help():
    print('Currently only print command is available, the syntax is: print(__<text u want to print>__) \n Example: print(__Hello world__)') 

clr()
def main():
    minp = input('HCOMPILER: ')
    num = len(minp)
    numa = num - 3
    inp1 = minp[0:5]

    if inp1 == 'print': 
        pinp = minp[8:numa]
        clr()
        print(pinp)
        main()
    elif inp1 == 'help':
        help()
        main()
    elif inp1 == 'clear' or inp1 == 'clr':
        clr()
        main()
    elif inp1 == 'exit':
        sys.exit()
    else:
        print('Wrong input')
        help()
        main()
main()
