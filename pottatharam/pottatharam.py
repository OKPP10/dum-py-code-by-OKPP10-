import random

def pottan():
    name = input('enter your name : ')
    r = random.randint(100, 2000)
    
    for i in range(r):
        print(name + ' pottan')

    print('your pottan score :' + str(r) + '\npretty good ;).')
    run_again = input('\n type q to quit or press enter to run again. \n')
    
    if run_again == 'q':
        quit()
    else:
        pottan()

pottan()
