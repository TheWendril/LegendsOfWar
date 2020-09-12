from src.render.screen import Screen
from src.countries.collection import germany
from src.render.menu import Menu
from Load import storage

sla = Screen.TerminalScreen()

p1 = germany.germany(5000)
p2 = germany.germany(4000)
p1.Army.buySoldiers(300)

men = Menu.RenderMenu()

storage.save({
    'Level' : 0,
    'Nome' : 'Germany vs England'
})

rdm = Menu.RenderMenu()
init = rdm.renderMainMenu()

if init == 0:

    rdm.renderDifficultyMenu()

    while 1:    

        sla.screenRender(p1, p2)
        
        if men.renderPlayerOptions() == 3:
            break


elif init == 1:

    lista = [str(x) for x in storage.load() if str(x) != '{' or str(x) != '}']
    rdm.renderRandomMenu(lista, 'Saves')


elif init == 3:

	aboutFile = open('./about/about.txt')
	txt = aboutFile.read()
	print(txt)
