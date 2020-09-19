class CPU:

    def __init__(self, Player, Machine):
        self.Player = Player
        self.Machine = Machine
        self.VictoryRate = 0

    def refresh(self, Player, Machine):
        self.Player = Player
        self.Machine = Machine

    def DefineStrategy(self):
    
        MachineDefense = [0,0,0]
        MachineBuy = [0,0,0]
        MachineAttack = [0,0,0]
        MachineResources = 0

        return {          

            'order': ['Soldiers', 'Ship', 'Airplanes'],
            'Buy': MachineBuy,
            'Attack': MachineAttack,
            'Defense' : MachineDefense,
            'Resources': MachineResources,
            'special': False
        
        }

