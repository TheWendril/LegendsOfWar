from .power import Power

class army:


    def __init__(self, SPrice, AirPrice, SHPrice, Soldiers = 0, Ships = 0, Airplanes = 0):

        self.Soldiers = Soldiers
        self.Ships = Ships
        self.Airplanes = Airplanes

        self.armyPower = Power()

        self.Prices = {
            'SPrice' : SPrice,
            'AirPrice': AirPrice,
            'SHPrice': SHPrice
        }       

    def armyStatus(self):

        return {
            'Soldiers' : self.Soldiers,
            'Ships' : self.Ships,
            'Airplanes' : self.Airplanes
        }


    def soldiersDamage(self):

        return self.Soldiers * self.armyPower.SOPower


    def shipDamage(self):

        return self.ShipDamage * self.armyPower.SHPower


    def airplaneDamage(self):

        return self.Airplanes * self.armyPower.AIRpower
    

    def buySoldiers(self, quantity):

        self.Soldiers += quantity
        return quantity * self.Prices['SPrice']
        
    def buyShips(self, quantity):

        self.Soldiers += quantity
        return quantity * self.Prices['SHPrice']
        
    def buyAirplanes(self, quantity):

        self.Airplanes += quantity
        return quantity * self.Prices['AIRPrice']
        

    def setPrices(self, SPrice, AirPrice, SHPrice):

        self.Prices['SPrice'] = SPrice
        self.Prices['AirPrice'] = AirPrice
        self.Prices['SHPrice'] = SHPrice