import time
import numpy
import math

def calc():
    print('----------------------------------------------------------------------------------------------------')
    print('1. addition')
    print('2. subtraction')
    print('3. multiplication')
    print('4. divition')
    print('5. square_root')
    print('----------------------------------------------------------------------------------------------------')
    met = input(1/2/3/4)
    if met == ('1'):
        print('You choosed addition.')
    elif met == ('2'):
        print('You choosed subtraction.')
    elif met == ('3'):
        print('You choosed multiplication.')
    elif met == ('4'):
        print('You choosed divition')
    elif met == ('5'):
        print('You choosed square_root')
    else:
        print(f'{met} is not a supported calculation method. Please input a supported method')
        time.sleep(1)
        calc()
    
    if met == ("1"):
        print("Please enter the first number.")
        num1 = input()
        print("Please enter the second number.")
        num2 = input()
        print(f'The answer is {int(num1) + int(num2)}')
        fin()
    elif met == ("2"):
        print("Please enter the first number.")
        num1 = input()
        print("Please enter the second number.")
        num2 = input()
        print(f'The answer is {int(num1) - int(num2)}')
        fin()
    elif met == ("3"):
        print("Please enter the first number.")
        num1 = input()
        print("Please enter the second number.")
        num2 = input()
        print(f'The answer is {int(num1) * int(num2)}')
        fin()
    elif met == ("5"):
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
