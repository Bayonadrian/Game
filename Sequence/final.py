# Importing libraries.
import Sequence.steps as steps
import Sequence.views as views
import Sequence.basics as basics
import Sequence.funtions as functions
import time
import os
import sys

# Final sreucture.
def final(health, branch):

    # While loop to receive commands.
    while True:

        # Asking for commands.
        commands = input('Give me the next command(ambulance) >>> ')

        # HELP command.
        if commands == 'help':

            print(steps.instructions_txt)

            time.sleep(1)

        # GET command.
        elif 'get' in commands:

            print('There is nothing to get')

        # CHARACTERS command.
        elif commands == 'characters':

            basics.characters()
            print('\n')

            time.sleep(1)

        # HEALTH command.
        elif commands == 'health':

            print(f'Gru has {health} hp', '\n')

            time.sleep(1)

        # GARDEN command.
        elif commands == 'garden':

            print('You cannot go to the garden right now', '\n')

            time.sleep(1)

        # HOUSE command.
        elif commands == 'house':

            print('You cannot go to the house right now')

        # INVENTORY command.
        elif commands == 'inventory':

            # Final instruction to finish the game.
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

        # DESCRIBE command.
        elif commands == 'describe':

            print(views.ambulance(), '\n')

            time.sleep(1)

        # EXIT command.
        elif commands == 'exit':

                print('Bye...')

                time.sleep(3)

                quit()

        # Else statement to validate the program
        else:

            print('I cannot recognize the command, but maybe you want to call a minion to distract the police officer', '\n')

            minion = input('Give me the name of the minion you want to call >>> ').lower()

            # Option two to finish the game.
            if 'bob' in minion:

                print('Bob has convinced the police officer...', '\n')

                print('Gru is gonna be ok... Game Over')

                # Asking to finish with the game.
                exit = input('Do you want to exit?(write exit to quit) >>>> ').lower()

                # Finishing the game.
                if exit == 'exit':

                    quit()

                # Restarting the game.
                else:

                    os.execl(sys.executable, sys.executable, *sys.argv)

            else:

                print(f'{minion} could not convinced the officers Gru lost 2 hp', '\n')

                time.sleep(2)

                health -= 2

            # Game over protocol.
            functions.game_over(health=health)

            # Sleeping 1 sec.
            time.sleep(1)