from Load import storage
from src.render.menu import Menu


storage.save({
    'Level' : 0,
    'Nome' : 'Germany vs England'
})


rdm = Menu.RenderMenu()
init = rdm.renderMainMenu()

if init == 0:

    rdm.renderDifficultyMenu()

elif init == 1:

    lista = [str(x) for x in storage.load() if str(x) != '{' or str(x) != '}']
    rdm.renderRandomMenu(lista, 'Saves')

