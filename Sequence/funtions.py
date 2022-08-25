from time import sleep
import os
import sys

def game_over(health):

    if health <= 0:

        print(f'Gru\'s health is {health}')
        sleep(1)
        print('Game Over')
        sleep(1)
        
        exit = input('Do you want to exit?(write exit to quit) >>>> ').lower()

        if exit == 'exit':

            quit()

        else:

            os.execl(sys.executable, sys.executable, *sys.argv)
