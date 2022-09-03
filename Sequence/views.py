import Sequence.funtions as functions
import os.path as path
import time

##### First room(garden)
def garden():

    # Garden description.
    garden_path= path.relpath('Mk/garden.md')

    with open(garden_path, 'r') as txt:

        return txt.read()

##### Fift room(ambulance)
def ambulance():

    # Ambulance description
    ambulance_path= path.relpath('Mk/ambulance.md')

    with open(ambulance_path, 'r') as txt:

        return txt.read()

#### Third room(house)
def house(instruction, health):

    # House description.
    house_path= path.relpath('Mk/house.md')

    house_text= ""

    inventory= False

    # House description.
    with open(house_path, 'r') as txt:

        house_text= txt.read()

    # House loop.
    while True:

        # Asking for commands.
        commands= input('Give me the next command(house) >>> ')

        # HELP command
        if commands == 'help':

            print(instruction)

            time.sleep(1)

        # GET command.
        elif commands == 'get':

            print('You got the inventory in the bag', '\n')

            inventory= True

        # CHARACTERS command.
        elif commands == 'characters':

            print('Kevin has great leadership skills...')
            print('Stuart has great memory...')
            print('And Bob... He is a great boy...')

            time.sleep(1)

        # HEALTH command.
        elif commands == 'health':

            print(health, '\n')

            time.sleep(1)

        # GARDEN command.
        elif commands == 'garden':

            print('Moving to the garden', '\n')

            time.sleep(1)

            return health, inventory

        # HOUSE command.
        elif commands == 'house':

            print('You are in the house right now!...', '\n')

            time.sleep(1)

        # INVENTORY command.
        elif commands == 'inventory':

            if inventory == False:

                print('You have to take the bag to see the objects within...', '\n')

            else:

                print('You have to be at the garden to use the items...', '\n')

        # DESCRIBE command.
        elif commands == 'describe':

            print(house_text)            

        # EXIT command.
        elif commands == 'exit':

            print('To exit the game you have to move to the garden', '\n')

            time.sleep(1)

        # Else statement to validate the program.
        else:

            print('I cannot recognize the command', '\n')

            health -= 1

            functions.game_over(health=health)

            time.sleep(1)
        

    