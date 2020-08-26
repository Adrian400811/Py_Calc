import time
import math


def calc():
    print('-'*100)
    print('1. addition')
    print('2. subtraction')
    print('3. multiplication')
    print('4. division')
    print('5. square_root')
    print('6. %')
    print('-'*100)
    met = input("input(1/2/3/4/5/6)")
    if met == '1':
        print('You chose addition.')
    elif met == '2':
        print('You chose subtraction.')
    elif met == '3':
        print('You chose multiplication.')
    elif met == '4':
        print('You chose division')
    elif met == '5':
        print('You chose square_root')
    elif met == '6':
        print('You chose %')
    else:
        print(f'{met} is not a supported calculation method. Please input a supported method')
        time.sleep(1)
        calc()
    
    if met == "1":
        print("Please enter the first number.")
        num1 = input()
        print("Please enter the second number.")
        num2 = input()
        print(f'The answer is {int(num1) + int(num2)}')
        fin()
    elif met == "2":
        print("Please enter the first number.")
        num1 = input()
        print("Please enter the second number.")
        num2 = input()
        print(f'The answer is {int(num1) - int(num2)}')
        fin()
    elif met == "3":
        print("Please enter the first number.")
        num1 = input()
        print("Please enter the second number.")
        num2 = input()
        print(f'The answer is {int(num1) * int(num2)}')
        fin()
    elif met == "5":
        print('Please enter the number')
        num1 = input()
        print(f'The answer is {math.sqrt(int(num1))}')
        fin()
    elif met == "6":
        print("please enter the first number")
        num1 = input()
        print('Please enter the second number')
        num2 = input()
        print(f"The answer is {(int(num1)) % (int(num2))}")
        fin()


def fin():
    print("Do you want to calculate another math?")
    leave = input("input(y/n)")
    if leave == "y":
        calc()
    elif leave == "n":
        print("Shutting Down")
        time.sleep(2)
        exit()
    else:
        print("I don't know what do you mean.")
        time.sleep(2)
        fin()


calc()
fin()
