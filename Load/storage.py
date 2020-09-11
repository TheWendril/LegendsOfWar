import json
import os
from src.menu import Menu

os.chdir('./Load')

def save(level):

    archive = open('saves.json', 'r')

    saves = json.load(archive)
    saves.append(level)

    archive.close()

    archive = open('saves.json', 'w')
    json.dump(saves, archive)
    

def load():

    archive = open('saves.json', 'r')
    MenuList = list(json.load(archive))

    [str(x) for x in MenuList]
        
    return Menu.RenderMenu.renderRandomMenu(MenuList, 'Loads')


