import Sequence.funtions as functions
import os.path as path
import time

def garden():

    garden_path= path.relpath('Mk/garden.md')

    with open(garden_path, 'r') as txt:

        return txt.read()

def ambulance():

    ambulance_path= path.relpath('Mk/ambulance.md')

    with open(ambulance_path, 'r') as txt:

        return txt.read()

def house(instruction, health):

    house_path= path.relpath('Mk/house.md')

    house_text= ""

    inventory= False

    with open(house_path, 'r') as txt:

        house_text= txt.read()

    while True:

        commands= input('Give me the next command(house) >>> ')

        if commands == 'help':

            print(instruction)

            time.sleep(1)

        elif commands == 'get':

            print('You got the inventory in the bag', '\n')

            inventory= True

        elif commands == 'characters':

            print('Kevin has great leadership skills...')
            print('Stuart has great memory...')
            print('And Bob... He is a great boy...')

            time.sleep(1)

        elif commands == 'health':

            print(health, '\n')

            time.sleep(1)

        elif commands == 'garden':

            print('Moving to the garden', '\n')

            time.sleep(1)

            return health, inventory

        elif commands == 'house':

            print('You are in the house right now!...', '\n')

            time.sleep(1)

        elif commands == 'inventory':

            if inventory == False:

                print('You have to take the bag to see the objects within...', '\n')

            else:

                print('You have to be at the garden to use the items...', '\n')

        elif commands == 'describe':

            print(house_text)            

        elif commands == 'exit':

            print('To exit the game you have to move to the garden', '\n')

            time.sleep(1)

        else:

            print('I cannot recognize the command', '\n')

            health -= 1

            functions.game_over(health=health)

            time.sleep(1)
        

    