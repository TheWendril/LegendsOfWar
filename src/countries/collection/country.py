from ...army.Army import army
from abc import ABC, abstractmethod

class country(ABC):

    def __init__(self):

        self.Money = None
        self.Army = None
        self.Builds = None   
        self.Life = None

   
    def setProperties(self, Money, Life):
        
        self.Money = Money
        self.Life = Life


    def addNewBuild(self, Build):

        if Build.count(Build) == 0:
            self.Builds.append(Build)
            return True
        
        else:
            return False

    def setArmyPower(self, Solpercent, Airpercent, SHpercent):

        self.Army.armyPower.setPower(Solpercent, Airpercent, SHpercent)


    def getProperties(self):

        return {
            'Money': self.Money,
            'Life': self.Life,
            'Army': self.Army
        }


    def getBuilds(self):
        return self.Builds

    @abstractmethod

    def special():
        pass