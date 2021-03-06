from simple_term_menu import TerminalMenu
import json
import os

archivePath = __file__[0 : len(__file__)  - 7] + 'menuLayout.json'

class RenderMenu:
    
    def __init__(self):
        
        archive = open(archivePath, 'r')
        self.MenuList = json.load(archive)

    def renderMainMenu(self):
            
        mainMenu = TerminalMenu(self.MenuList[0], title = '\nLegends of War\n')
        return mainMenu.show()

    def renderDifficultyMenu(self):

        mainMenu = TerminalMenu(self.MenuList[1], title = 'Choose Your Difficulty')
        return mainMenu.show()

    def renderSelectCountry(self):

        mainMenu = TerminalMenu(self.MenuList[2], title = 'Choose Your Country')
        return mainMenu.show()

    def renderPlayerOptions(self):
        
        mainMenu = TerminalMenu(self.MenuList[3])
        return mainMenu.show()

    def renderExit():
        mainMenu = TerminalMenu(self.MenuList[4])

    @staticmethod

    def renderRandomMenu(MenuList, MenuTitle):

        mainMenu = TerminalMenu(MenuList, title= MenuTitle)
        return mainMenu.show()
