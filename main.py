import Sequence.steps as steps
import Sequence.basics as basics
import Sequence.views as views
import Sequence.decisions as decisions
import Sequence.sequence as sequence
import Sequence.funtions as functions
import time

while True:

    inventory= False

    health= 8

    branch_get= False

    print(steps.title_txt)

    time.sleep(2)

    print(steps.instructions_txt, '\n')

    time.sleep(3)

    print(steps.start_txt)

    time.sleep(3)

    print('To start take a look of your items...', '\n')

    basics.items_first()

    time.sleep(1)

    while True:

        start_playing= input('Let me know when you are ready(write ok) >>> ').lower()

        if start_playing == 'ok':

            break

        else:

            pass

    time.sleep(1)

    print('Let\'s see the scenary', '\n')

    time.sleep(1)

    print(sequence.f_sequence_txt, '\n')

    time.sleep(3)

    f_desc= decisions.f_decision()

    health -= f_desc

    time.sleep(1)

    print(f'Gru now has {health} of hp, be careful!', '\n')

    time.sleep(1)

    print('Gru is injured, and the minions want to help him to feel better...')

    time.sleep(1)

    print('I recommend to describe the characters...', '\n')

    time.sleep(1)

    characters= input('Write "characters" to know your characters >>> ').lower()

    if characters == 'characters':

        print('\n')

        basics.characters()
        
        print('\n')
 
    time.sleep(1)

    while True:

        commands = input('Give me the next command(garden) >>> ')

        if commands == 'help':

            print(steps.instructions_txt)

            time.sleep(1)

        elif 'get' in commands:

            branch= input('Do you want to get a branch >>>> ')

            if 'no' in branch:

                print('You did not get anything', '\n')

            else:

                branch_get= True

                print('You got a branch which is totally useless', '\n')

        elif commands == 'characters':

            basics.characters()
            print('\n')

            time.sleep(1)

        elif commands == 'health':

            print(f'Gru has {health} hp', '\n')

            time.sleep(1)

        elif commands == 'garden':

            print('You are in the garden right now!!', '\n')

            time.sleep(1)

        elif commands == 'house':

            desc, inventory = views.house(instruction= steps.instructions_txt, health= health)

            health = desc

        elif commands == 'inventory':

            if inventory == False:

                print('You have to take the bag to see the objects within...', '\n')

            else:

                health= basics.items(health= health, branch= branch_get)

                print(f'Gru has {health} hp', '\n')

        elif commands == 'describe':

            print(views.garden(), '\n')

            time.sleep(1)

        elif commands == 'exit':

            quit()

        else:

            print('I cannot recognize the command', '\n')

            health -= 1

            functions.game_over(health=health)

            time.sleep(1)