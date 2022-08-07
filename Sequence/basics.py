import random

def username():

    username= input('Please give me your name >>> ')

    return username

def calling():

    try:

        health= 0

        while True:

            number= round(float(input('Write the number to call >>> ')))

            if number == 911:

                return health

            else:

                print('Nobody answered... Try again', '\n')

                print('Gru lost 1 hp', '\n')
            
                health += 1

    except:

        print('Please write a number', '\n')

        calling()

def cellphone():

        print('Do you want to make a call?', '\n')

        health= 0

        while True:

            to_call= input('Who is gonna make the call (write Kevin, Stuart, Bob or Gru) >>> ')

            subjects= ['Kevin', 'Stuart', 'Bob', 'Gru']

            machine= random.choice(subjects)

            if to_call == 'Gru':

                return health + calling()

            elif to_call == machine:

                return health + calling()

            else:

                print(f'{to_call} cannot talk because he is very nervous... Try again', '\n')

                print('Gru lost 1 hp', '\n')

                health += 1

def banana():

        print('This is a banana and is totally useless... Try again', '\n')

        print('Gru lost 1 hp', '\n')

        return 1

        

def fak():

        print('First aid kit, but minions doesn\'t know how to use it and they are gonna make several mistakes... Try again', '\n')

        print('Gru lost 3 hp', '\n')

        return 3

def items_first():

    while True:

        print('You have three items:', 'cellphone', '-', 'banana', '-', 'first aid kit', '\n')

        item= input('Let me know which one do you want(write the name) >>> ').lower()

        if item == 'cellphone':

            print('You have choosen the cellphone...', '\n')
            break

        elif item == 'banana':

            print('You have choosen the banana...', '\n')
            break

        elif item == 'first aid kit':

            print('You have choosen the first aid kit...', '\n')
            break

        else:

            print('I cannot understand well... Please try again', '\n')

def items():

    health= 0

    while True:

        print('You have three items:', 'cellphone', '-', 'banana', '-', 'first aid kit', '\n')

        item= input('Let me know which one do you want(write the name) >>> ').lower()

        if item == 'cellphone':

            health += cellphone()
            return health

        elif item == 'banana':

            health += banana()

        elif item == 'first aid kit':

            health += fak()

        else:

            print('I cannot understand well... Please try again', '\n')
            print('Gru lost 1 hp', '\n')

            health += 1


