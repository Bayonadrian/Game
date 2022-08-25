import os.path as path

istructions_path= path.realpath('Mk/instructions.md')
title_path= path.realpath('Mk/title.md')
start_path= path.realpath('Mk/start.md')

def title(text):

    with open(text, 'r') as txt:

        return txt.read()

def instructions(text):

    with open(text, 'r') as txt:

        return txt.read()

def start(text):
    
    with open(text, 'r') as txt:

        return txt.read()


instructions_txt= instructions(istructions_path)
title_txt= title(title_path)
start_txt= start(start_path)