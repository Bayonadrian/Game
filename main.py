import Sequence.steps as steps
import Sequence.basics as basics
import Sequence.views as views
import Sequence.decisions as decisions
import time

while True:

    health= 8

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

    print(views.f_view_txt, '\n')

    time.sleep(3)

    f_desc= decisions.f_decision()

    health -= f_desc

    time.sleep(1)

    print(f'Gru now has {health} of hp, be careful!', '\n')

    time.sleep(1)

    print(views.s_view_txt, '\n')

    time.sleep(3)

    s_desc= decisions.s_decision()

    time.sleep(2)

    health -= s_desc

    if health <= 0:

        print('Game over, Gru died')
        
        go= input('Press 1 to restart, otherwise the game is gonna finish >>> ')

        if go == '1':

            continue

        else:

            quit()

    print(f'Gru has {health} of hp. Be careful!', '\n')

    time.sleep(2)

    print(views.t_view_txt)

    time.sleep(4)

    t_desc= decisions.t_decision()

    health -= t_desc

    print(f'Gru has {health} of hp', '\n')

    if t_desc > 0:

        print('Gru avoided jail and stole the moon successfully.', '\n')

        print('Game over', '\n')

    else:

        print('Gru survived but stayed in the jail for a while.')

        print('Game over', '\n')

    stop_game= input('Do you want to play again?(press 1) >>> ')

    if stop_game == '1':

        continue

    else:

        quit()