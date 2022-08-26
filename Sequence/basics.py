from time import sleep
import Sequence.funtions as functions
import Sequence.final as final
import random

def characters():

    print('Kevin has great leadership skills...')
    print('Stuart has great memory...')
    print('And Bob... He is a great boy...')

def calling(health, branch):

    try:

        while True:

            asking= input('Do you wanna ask someone(write Kevin, Stuart or Bob) >>> ')

            if asking == 'Stuart':

                print('I have an idea, call 911')

            elif asking == 'Kevin':

                print('Call 12345!')

            elif asking == 'Bob':

                print('I just don\'t know what to do')

            number= round(float(input('Write the number to call >>> ')))

            if number == 911:

                print('Well done there is an ambulance on the way...', '\n')

                sleep(2)

                print('You are in the ambulance right now but there are some police officers who are trying to get Gru to the jail', '\n')

                sleep(2)

                print('You have to distract the police officers until the ambulance start moving', '\n')

                sleep(2)

                final.final(health=health, branch=branch)

            else:

                print('Nobody answered... Try again', '\n')
            
                health -= 1

                functions.game_over(health=health)

                print(f'Be careful Gru has {health} hp', '\n')

    except:

        health -= 1

        print('Please write a number', '\n')

        print(f'Be careful Gru has {health} hp', '\n')

        functions.game_over(health=health)

        calling()

def cellphone(health, branch):

        print('Do you want to make a call?', '\n')

        while True:

            to_call= input('Who is gonna make the call (write Kevin, Stuart, Bob) >>> ')

            subjects= ['Kevin', 'Stuart', 'Bob']

            machine= random.choice(subjects)

            if to_call == 'Kevin':

                return calling(health, branch)

            elif to_call == machine:

                return calling(health, branch)

            else:

                print(f'{to_call} cannot talk because he is very nervous... Try again', '\n')

                health -= 1

                functions.game_over(health=health)

                print(f'Be careful Gru has {health} hp', '\n')

def banana(health):

        health -= 1

        print('This is a banana and is totally useless... Try again', '\n')
        print(f'Be careful Gru has {health} hp', '\n')

        functions.game_over(health=health)

        return health

        
def fak(health):

        health -= 1

        print('First aid kit, but minions doesn\'t know how to use it and they are gonna make several mistakes... Try again', '\n')
        print(f'Be careful Gru has {health} hp', '\n')

        functions.game_over(health=health)

        return health

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

def items(health, branch):

    while True:

        print('You are in the inventory there you just have three commands...', '\n')

        sleep(1)

        print('cellphone', '-', 'banana', '-', 'first aid kit', '-', 'garden', '-', 'health', '\n')

        item= input('Let me know which one do you want(write the name) >>> ').lower()

        if item == 'cellphone':

            health = cellphone(health= health, branch= branch)

        elif item == 'banana':

            health = banana(health= health)

        elif item == 'first aid kit':

            health = fak(health= health)

        elif item == 'garden':

            return health

        elif item == health:

            print(f'Gru has {health} hp')

        else:

            print('I cannot understand well... Please try again', '\n')

            health -= 1

            functions.game_over(health=health)

            print(f'Be careful Gru has {health} hp', '\n')