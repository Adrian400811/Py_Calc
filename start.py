import time
import numpy
import math

def calc():
    print('addition(+) subtraction(-) multiplication(*) divition(/) square_root(sq_rt)?')
    met = input()
    if met == ('+'):
        print('You choosed addition.')
    elif met == ('-'):
        print('You choosed subtraction.')
    elif met == ('*'):
        print('You choosed multiplication.')
    elif met == ('/'):
        print('You choosed divition')
    elif met == ('sq_rt'):
        print('You choosed square_root')
    else:
        print(f'{met} is not a supported calculation method. Please input a supported method')
        time.sleep(1)
        calc()
    
    if met == ("+"):
        print("Please enter the first number.")
        num1 = input()
        print("Please enter the second number.")
        num2 = input()
        print(f'The answer is {int(num1) + int(num2)}')
        fin()
    elif met == ("-"):
        print("Please enter the first number.")
        num1 = input()
        print("Please enter the second number.")
        num2 = input()
        print(f'The answer is {int(num1) - int(num2)}')
        fin()
    elif met == ("*"):
        print("Please enter the first number.")
        num1 = input()
        print("Please enter the second number.")
        num2 = input()
        print(f'The answer is {int(num1) * int(num2)}')
        fin()
    elif met == ("sq_rt"):
        print('Please enter the number')
        num1 = input()
        print(f'The answer is {math.sqrt(int(num1))}')
        fin()

def fin():
    print("Do you want to calculate another math?")
    leave = input("y/n")
    if leave == "y":
        calc()
    elif leave == "n":
        print("Thanks for using our service.")
        time.sleep
        exit()
    else:
        print("I don't know what do you mean.")
        time.sleep(2)
        fin()

calc()
fin()
