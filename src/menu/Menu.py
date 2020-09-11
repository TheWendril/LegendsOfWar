from simple_term_menu import TerminalMenu
import json
import os

class RenderMenu:
    
    def __init__(self):

        os.chdir('./src/menu/')
        archive = open('menuLayout.json', 'r')
        self.MenuList = json.load(archive)

    def renderMainMenu(self):
            
        mainMenu = TerminalMenu(self.MenuList[0], title = 'Legends of War')
        return mainMenu.show()

    def renderDifficultyMenu(self):

        mainMenu = TerminalMenu(self.MenuList[1], title = 'Choose Your Difficulty')
        return mainMenu.show()

    def renderSelectCountry(self):

        mainMenu = TerminalMenu(self.MenuList[2], title = 'Choose Your Country')
        return mainMenu.show()


    @staticmethod

    def renderRandomMenu(MenuList, MenuTitle):

        mainMenu = TerminalMenu(MenuList, title= MenuTitle)
        return mainMenu.show()
