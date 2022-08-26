import Sequence.steps as steps
import Sequence.views as views
import Sequence.basics as basics
import Sequence.funtions as functions
import time
import os
import sys

def final(health, branch):

    while True:

        commands = input('Give me the next command(ambulance) >>> ')

        if commands == 'help':

            print(steps.instructions_txt)

            time.sleep(1)

        elif 'get' in commands:

            print('There is nothing to get')

        elif commands == 'characters':

            basics.characters()
            print('\n')

            time.sleep(1)

        elif commands == 'health':

            print(f'Gru has {health} hp', '\n')

            time.sleep(1)

        elif commands == 'garden':

            print('You cannot go to the garden right now', '\n')

            time.sleep(1)

        elif commands == 'house':

            print('You cannot go to the house right now')

        elif commands == 'inventory':

            if branch == True:

                invent= input('You have four items Banana, Cellphone, First aid kit and a Branch, select one >>> ').lower()

                if 'branch' in invent:

                    print('You smashed the police officer in the head with the branch, Gru is gonna be ok... Game over', '\n')

                    exit = input('Do you want to exit?(write exit to quit) >>>> ').lower()

                    if exit == 'exit':

                        sys.exit()

                    else:

                        os.execl(sys.executable, sys.executable, *sys.argv)

            else:

                print('You have three items Banana, Cellphone, First aid kit no one seems to be useful.', '\n')
                print('I suggest to invent a new command')

        elif commands == 'describe':

            print(views.ambulance(), '\n')

            time.sleep(1)

        elif commands == 'exit':

                print('Bye...')

                time.sleep(3)

                quit()

        else:

            print('I cannot recognize the command, but maybe you want to call a minion to distract the police officer', '\n')

            minion = input('Give me the name of the minion you want to call >>> ').lower()

            if 'bob' in minion:

                print('Bob has convinced the police officer...', '\n')

                print('Gru is gonna be ok... Game Over')

                exit = input('Do you want to exit?(write exit to quit) >>>> ').lower()

                if exit == 'exit':

                    quit()

                else:

                    os.execl(sys.executable, sys.executable, *sys.argv)

            else:

                print(f'{minion} could not convinced the officers Gru lost 2 hp', '\n')

                time.sleep(2)

                health -= 2

            functions.game_over(health=health)

            time.sleep(1)