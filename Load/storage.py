import json
from src.render.menu import Menu

archivePath = __file__[0 : len(__file__) - 10] + 'saves.json'

def save(level):

    archive = open(archivePath, 'r')

    saves = json.load(archive)
    saves.append(level)

    archive.close()

    archive = open(archivePath, 'w')
    json.dump(saves, archive)
    

def load():

    archive = open(archivePath, 'r')
    MenuList = list(json.load(archive))

    [str(x) for x in MenuList]
        
    return MenuList


