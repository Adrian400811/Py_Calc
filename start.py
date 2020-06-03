import time

print("please enter ur name (just hit enter if you don't want to type).")
name = input()
print('Hi ' + name +'.')
time.sleep(2)
print('Do you want to calculate addition(+) subtraction(-) multiplication(*) or divition(/)?')
calc = input()
if calc == ('+'):
    print('You choosed addition.')
elif calc == ('-'):
    print('You choosed subtraction.')
elif calc == ('*'):
    print('You choosed multiplication.')
elif calc == ('/'):
    print('You choosed divition')
else:
    print('This is not a supported calculation methon. Thanks for using our service')
