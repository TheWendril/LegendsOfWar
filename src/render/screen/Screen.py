import os

class TerminalScreen:

    def __init__(self):
        NotImplemented

    def screenRender(self, Country1, Country2):

        os.system('cls' if os.name == 'nt' else 'clear')

        print(F"""
{Country1.Name}                                                        {Country2.Name}                                                                        

Life: {Country1.Life}                                                   Life: {Country2.Life}
Money: {Country1.Money}                                                 Money: {Country2.Money}        
Soldiers:  
AirPlanes:
Ships:



        """)
