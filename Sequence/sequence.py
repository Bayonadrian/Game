import os.path as path

f_sequence_path= path.relpath('Mk/f_sequence.md')
s_sequence_path= path.relpath('Mk/s_sequence.md')
t_sequence_path= path.relpath('Mk/t_sequence.md')

def f_view():

    with open(f_sequence_path, 'r') as view:

        return view.read()

def s_view():

    with open(s_sequence_path, 'r') as view:

        return view.read()

def t_view():

    with open(t_sequence_path, 'r') as view:

        return view.read()

f_sequence_txt= f_view()
s_sequence_txt= s_view()
t_sequence_txt= t_view()