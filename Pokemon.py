class Pokemon:
    def __init__(self, id, max_health, power):
        self.max_health = max_health
        self.health = max_health
        self.power = power
        self.id = id

        if(self.id == 0):
            self.name = "pikachu"
        if(self.id == 1):
            self.name = "charmander"
        if(self.id == 2):
            self.name = "bulbasaur"
        if(self.id == 3):
            self.name = "zoobat"
        if(self.id == 4):
            self.name = "pidgeotto"

    def __str__(self):
        return str(self.name) + " hp: " + str(self.health) + " att: " + str(self.power)

