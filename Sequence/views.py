import os.path as path

f_view_path= path.realpath('Game/Mk/f_place.md')
s_view_path= path.realpath('Game/Mk/s_place.md')
t_view_path= path.realpath('Game/Mk/t_place.md')

def f_view():

    with open(f_view_path, 'r') as view:

        return view.read()

def s_view():

    with open(s_view_path, 'r') as view:

        return view.read()

def t_view():

    with open(t_view_path, 'r') as view:

        return view.read()

f_view_txt= f_view()
s_view_txt= s_view()
t_view_txt= t_view()