# Importing libraries with videogame basics.
import Sequence.steps as steps
import Sequence.basics as basics
import Sequence.views as views
import Sequence.decisions as decisions
import Sequence.sequence as sequence
import Sequence.funtions as functions

# Importing time library.
import time

# While loop to iterate the game.
while True:

    # Setting the inventory as False.
    inventory= False

    # Setting health.
    health= 8

    # Setting branch as False.
    branch_get= False

    # Printing title.
    print(steps.title_txt)

    # Sleeping for 2 seconds.
    time.sleep(2)

    # Printing instructions.
    print(steps.instructions_txt, '\n')

    # Sleeping for 3 seconds.
    time.sleep(3)

    # Printing the start text.
    print(steps.start_txt)

    # Sleeping for 3 seconds.
    time.sleep(3)

    print('To start take a look of your items...', '\n')

    # Showing the items sample.
    basics.items_first()

    # Sleeping for 1 second.
    time.sleep(1)

    # While loop to start game
    while True:
        
        # Imput to start.
        start_playing= input('Let me know when you are ready(write ok) >>> ').lower()

        if start_playing == 'ok':

            # Start game.
            break

        else:

            pass
    
    # Sleeping for 1 second.
    time.sleep(1)

    print('Let\'s see the scenary', '\n')

    # Sleeping for 1 second.
    time.sleep(1)

    # Printing the first sequence.
    print(sequence.f_sequence_txt, '\n')

    # Sleeping for 3 seconds.
    time.sleep(3)

    ##### First room.
    f_desc= decisions.f_decision()

    # Starting health.
    health -= f_desc

    # Sleeping for 1 second.
    time.sleep(1)

    # Printing the Gru's health.
    print(f'Gru now has {health} of hp, be careful!', '\n')

    # Sleeping for 1 second.
    time.sleep(1)

    print('Gru is injured, and the minions want to help him to feel better...')

    # Sleeping for 1 second.
    time.sleep(1)

    # Recommending to describe the characters.
    print('I recommend to describe the characters...', '\n')

    # Sleeping for 1 second.
    time.sleep(1)

    # Asking for "characters" command.
    characters= input('Write "characters" to know your characters >>> ').lower()

    if characters == 'characters':

        print('\n')

        # Describing characters.
        basics.characters()
        
        print('\n')
    
    # Sleeping for 1 second.
    time.sleep(1)

    ##### Second room(garden).
    # While loop to start asking commands.
    while True:

        # Getting commands for the garden.
        commands = input('Give me the next command(garden) >>> ').lower()

        # Help command.
        if commands == 'help':
            
            # Printing instructions.
            print(steps.instructions_txt)

            # Sleeping for 1 second.
            time.sleep(1)

        # Get command.
        elif 'get' in commands:
            
            # Getting the branch.
            branch= input('Do you want to get a branch >>>> ').lower()

            if 'no' in branch:

                print('You did not get anything', '\n')

            else:

                # Changing the status of the branch.
                branch_get= True

                print('You got a branch which is totally useless', '\n')

        # Characters command.
        elif commands == 'characters':

            # Characters description.
            basics.characters()
            print('\n')

            time.sleep(1)

        # Health command.
        elif commands == 'health':

            # Printing the Gru's hp.
            print(f'Gru has {health} hp', '\n')

            time.sleep(1)

        # Garden command.
        elif commands == 'garden':

            print('You are in the garden right now!!', '\n')

            time.sleep(1)

        # House command.
        elif commands == 'house':

            # Calling and getting the results of the second room.
            desc, inventory = views.house(instruction= steps.instructions_txt, health= health)

            # Stablishing the Gru's hp.
            health = desc

        # Inventory command.
        elif commands == 'inventory':

            # If else statement to access to the inventory.
            if inventory == False:

                print('You have to take the bag to see the objects within...', '\n')

            else:

                # Accessing to the inventory.
                health= basics.items(health= health, branch= branch_get)

                # Printing the Gru's hp.
                print(f'Gru has {health} hp', '\n')

        # Describe command.
        elif commands == 'describe':
            
            # Describing the surroundings.
            print(views.garden(), '\n')

            time.sleep(1)

        # Exit command.
        elif commands == 'exit':

            # Finishing the game.
            quit()

        # Else statement to validate the game.
        else:

            print('I cannot recognize the command', '\n')

            # Decresing the Gru's hp.
            health -= 1

            # Finishing the program if Gru has less than 0 hp.
            functions.game_over(health=health)

            # Sleeping for 1 second.
            time.sleep(1)