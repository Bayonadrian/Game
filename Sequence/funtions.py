# Importing libraries sleep, os and sys.
from time import sleep
import os
import sys

# Game over protocol.
def game_over(health):

    # If else sentence to define if Gru's life is less than 0.
    if health <= 0:

        # Printing the Gru's life.
        print(f'Gru\'s health is {health}')
        # Sleepingo for 1 sec.
        sleep(1)
        # Printing game over.
        print('Game Over')
        # Sleeping 1 sec.
        sleep(1)
        
        # Option to exit or continue.
        exit = input('Do you want to exit?(write exit to quit) >>>> ').lower()

        # Finishing game.
        if exit == 'exit':

            quit()

        # Restarting the game.
        else:

            os.execl(sys.executable, sys.executable, *sys.argv)
