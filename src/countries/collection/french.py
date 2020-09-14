from .country import country
from ...army.Army import army


class japan(country):

    def __init__(self, initialMoney, soldiers, ships, airplanes):
        
        self.Name = 'England'
        self.Money = initialMoney
        self.Life = 6000
        self.Army = army(20, 150, 400, Soldiers= soldiers, Ships= ships, Airplanes= airplanes)
        self.Builds = []

    def special(self):

        self.Army.buySoldiers(250)
        self.Army.armyPower.setPower(30, 0, 0)