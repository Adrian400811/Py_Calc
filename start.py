import time
import numpy
import math

def calc():
    print('addition(+) subtraction(-) multiplication(*) divition(/) square_root(sq_rt)?')
    calc = input()
    if calc == ('+'):
        print('You choosed addition.')
    elif calc == ('-'):
        print('You choosed subtraction.')
    elif calc == ('*'):
        print('You choosed multiplication.')
    elif calc == ('/'):
        print('You choosed divition')
    elif calc == ('sq_rt'):
        print('You choosed square_root')
    else:
        print(f'{calc} is not a supported calculation methon. Thanks for using our service')
        time.sleep(2)
        exit()

    num1 = 0
    num2 = 0

    def numbers():
        print("Please enter the first number.")
        num1 = input()
        print("Please enter the second number.")
        num2 = input()

    if calc == ("+"):
        numbers()
        print(f'The answer is {int(num1) + int(num2)}')
        fin()
    elif calc == ("-"):
        numbers()
        print(f'The answer is {int(num1) - int(num2)}')
        fin()
    elif calc == ("*"):
        numbers()
        print(f'The answer is {int(num1) * int(num2)}')
        fin()
    elif calc == ("sq_rt"):
        print('Please enter the number')
        num1 = input()
        print(f'The answer is {math.sqrt(num1)}')
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
