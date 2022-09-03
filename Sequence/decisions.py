import Sequence.basics as basics
import time

# First decision.
def f_decision():

    # Loop for the first decision.
    while True:
 
        print('You have to take the first decision...', '\n')
        
        time.sleep(1)
        decision= input('Press 0 to keep the peel or 1 to throw it >>> ')

        # If else statement to decide the game starting.
        if decision == '0':

            print('You keep the peel. So, when Gru started moving, he fell into a hole and suffered several serious injuries. You lost 2 hp', '\n')

            return 2
            break

        if decision == '1':

            print('You throw the peel. So, when Gru started moving, he slipped with the peel and fell to the ground; now, he suffered serious injuries. You lost 1 hp', '\n')
            
            return 1
            break

        else:

            print('Please select a correct answer... Try again.', '\n')

# Secon decision.
def s_decision():

    return basics.items()